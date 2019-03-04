# SLCAirQuality
python script to pull AQI readings from PurpleAir sensors and tweet hourly updates [@SLCAirQuality](https://twitter.com/slcairquality)

## Libraries Used:
* [python-aqi](https://pypi.org/project/python-aqi/) - convert PM2.5 measurements to AQI values
* [tweepy](https://github.com/tweepy/tweepy) - connect to Twitter
* [requests](https://pypi.org/project/requests/) - parse JSON from PurpleAir
* [schedule](https://pypi.org/project/schedule/) - schedule regular tweets

## Notes
* You'll need to apply for a [Twitter developer account](https://developer.twitter.com/en/apply-for-access.html) to generate the API keys and tokens 
* Info on PurpleAir API [here](https://github.com/bomeara/purpleairpy/blob/master/api.md)
* To find the Sensor ID, search the name of the sensor [here](https://www.purpleair.com/json), then pull individual sensor data at https://www.purpleair.com/json?show=ID
