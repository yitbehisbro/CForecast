#!/usr/bin/python3
""" A module used to forecast a n-days weather data """
import requests
from geopy.geocoders import Nominatim
import pandas as pd


def coordinate(city=None):
    """ Converts the city name to its coordinate """
    geolocator = Nominatim(user_agent="CForecast")
    location = geolocator.geocode(city)
    coord = {"lat": round(location.latitude, 2),
             "lon": round(location.longitude, 2)}
    return coord


def weather_data(forecast_days, city=None):
    """ Returns the weather data of a city """
    coord = coordinate(city)
    print(coord)
    url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&daily=weathercode,temperature_2m_max," \
          "temperature_2m_min,sunrise,sunset&forecast_days={}&timezone=Africa%2FCairo".format(coord['lat'],
                                                                                              coord['lon'],
                                                                                              forecast_days)
    req = requests.get(url)
    result = req.json()
    return result


def weather_code(code=None):
    """ Converts weather code to phrases """
    codes_data = {'0': 'Clear sky', '1': 'Mainly clear', '2': 'Partly cloudy', '3': 'Overcast clouds',
                  '45': 'Fog', '48': 'Depositing rime fog', '51': 'Drizzle light rain',
                  '53': 'Drizzle moderate rain', '55': 'Dense intensity', '56': 'Light Freezing Drizzle',
                  '57': 'Dense intensity Freezing Drizzle', '61': 'Slight rain', '63': 'Moderate rain',
                  '65': 'Heavy intensity rain', '66': 'Light Freezing Rain', '67': 'Heavy intensity Freezing Rain',
                  '71': 'Slight snow fall', '73': 'Moderate snow fall', '75': 'Heavy intensity snow fall',
                  '77': 'Snow grains', '80': 'Slight Rain showers', '81': 'Moderate rain showers',
                  '82': 'Violent rain showers',
                  '85': 'Slight Snow showers', '86': 'Heavy Snow showers', '95': 'Thunderstorm: Slight or moderate',
                  '96': 'Thunderstorm with slight hail', '99': 'Thunderstorm with heavy hail'}
    if code is None:
        return None
    return codes_data[str(code)]


def refine_data(forecast_days, city=None):
    """ Refines the data in meaningful way """
    if forecast_days > 16:
        return "Unfortunately, I can not do a forecast for more than 16 days.\nSorry for that."
    weather = weather_data(forecast_days, city)
    output = ""
    dates = weather['daily']['time']
    summary = weather['daily']['weathercode']
    temp_min = weather['daily']['temperature_2m_min']
    temp_max = weather['daily']['temperature_2m_max']

    for i in range(len(dates)):
        output += "⌚ On {} ({}):\n\t🌡 Max temp: {} ℃,\n\t🌡 Min temp: {} ℃\n\t⛅ It will be: {}.\n\n\n".format(
            pd.Timestamp(dates[i]).day_name(), dates[i], temp_max[i], temp_min[i], weather_code(summary[i]))
    return output
