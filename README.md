# SLCAirQuality
python script to pull AQI readings from PurpleAir sensors and tweet hourly updates [@SLCAirQuality](https://twitter.com/slcairquality)

## Libraries Used:
* [requests](https://pypi.org/project/requests/) - parse JSON from PurpleAir
* [python-aqi](https://pypi.org/project/python-aqi/) - convert PM2.5 measurements to AQI values
* [tweepy](https://github.com/tweepy/tweepy) - connect to Twitter
* [schedule](https://pypi.org/project/schedule/) - schedule regular tweets

## Notes
* You'll need to apply for a [Twitter developer account](https://developer.twitter.com/en/apply-for-access.html) to generate the API keys and tokens 
* Info on PurpleAir API [here](https://github.com/bomeara/purpleairpy/blob/master/api.md)
  * The temperature sensor inside PurpleAir sensors measures the inside of the sensor housing, not ambient conditions. On the PurpleAir map, 7 ºF is subtracted from the raw temperature values to "better fit" ambient conditions.
* To find the Sensor ID, search the name of the sensor [here](https://www.purpleair.com/json), then pull individual sensor data at https://www.purpleair.com/json?show=ID
