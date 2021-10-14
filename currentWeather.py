#! /usr/bin/python3
#currentWeather.py - Prints the weather for a location from the command line
#if this doesn't work - please collect new API key
APPID = '7c1407c9d3b986205d68de5b4712d4e6'
import json
import requests
import sys
import pprint


if len(sys.argv) < 2:
    print('Usage: get OpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ''.join(sys.argv[1:])
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (location, APPID)
response = requests.get(url)
response.raise_for_status()
#uncomment to see the raw json txt:
#print(response.text)
weatherData = json.loads(response.text)
#pprint.pprint(weatherData)
#print weather descriptions
w = weatherData
print('Current weather in %s:' % (location))
print(w['weather'][0]['main'], '-', w['weather'][0]['description'])
print(str(int(int(w['main']['temp']) - 273.15)) + ' °C')
