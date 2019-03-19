#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://github.com/bomeara/purpleairpy/blob/master/api.md
# https://pypi.org/project/python-aqi/
# All sensors found at https://www.purpleair.com/json
# specific sensors found by searching ID: https://www.purpleair.com/json?show=
# sensors used:
# Downtown: KSL Triad (SensorID: 5014)
# Avenues: Zivio (SensorID: 12987)
# South Salt Lake: 3450 South 500 East  (SensorID: 6434)
# U of U: Douglas 2 (SensorID: 1539)
# Park City: April Mountain, Park City, UT (SensorID: 12861)
import aqi
import json
import requests
import schedule
import time
import tweepy


class Sensor:
    name = None
    ID = None
    temp = None
    age = None
    lastSeen = None
    pm2_5 = None
    AQI = None


downtown = Sensor()
downtown.name = "Downtown: "
downtown.ID = "5014"
avenues = Sensor()
avenues.name = "Avenues: "
avenues.ID = "12987"
southSaltLake = Sensor()
southSaltLake.name = "South Salt Lake: "
southSaltLake.ID = "6434"
uOfU = Sensor()
uOfU.name = "U of U: "
uOfU.ID = "1539"
parkCity = Sensor()
parkCity.name = "Park City: "
parkCity.ID = "12861"
sensors = [downtown, avenues, southSaltLake, uOfU, parkCity]


# == Tweepy Authentication ==
def authenticate():
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    global api
    api = tweepy.API(auth)
    print(api.me().name)


def updateSensorData():
    for sensor in sensors:
        response = requests.get(url='https://www.purpleair.com/json?show=' + sensor.ID)
        data = response.json()
        sensor.age = data['results'][0]['AGE']
        sensor.lastSeen = data['results'][0]['LastSeen']
        sensor.pm2_5 = data['results'][0]['PM2_5Value']
        sensor.temp = str(int(data['results'][0]['temp_f']) - 7)  # the temperature sensor inside PurpleAir sensors
        # measure the inside of the sensor housing, not ambient conditions. On the PurpleAir map, 7F is subtracted from
        # the raw temperature values to "better fit" ambient conditions.
        sensor.AQI = aqi.to_iaqi(aqi.POLLUTANT_PM25, sensor.pm2_5, algo=aqi.ALGO_EPA)
        # print(json.dumps(data, indent=4))
    # for sensor in sensors:
    #     print(vars(sensor))


def tweet():
    message = "Current AQI:\n"
    for sensor in sensors:
        message += sensor.name + str(sensor.AQI) + "\n"
    api.update_status(message)
#     print(message)


def job():
    updateSensorData()
    tweet()


authenticate()
updateSensorData()
tweet() # tweet once now
schedule.every(1).hour.do(job)
while True:  # tweet every hour going forward
    schedule.run_pending()
    time.sleep(1)
