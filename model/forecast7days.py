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


def weather_data(city=None):
    """ Retuns the weather data of a city """
    coord = coordinate(city)
    print(coord)
    url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,precipitation_hours,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant&timezone=Africa%2FCairo".format(coord['lat'], coord['lon'])
    req = requests.get(url)
    result = req.json()
    return result

def refine_data(city=None):
    """ Refines the data in meaningful way """
    weather = weather_data(city)
    output = ""
    dates = weather['daily']['time']
    summary = weather['daily']['weathercode']
    temp_min = weather['daily']['temperature_2m_min']
    temp_max = weather['daily']['temperature_2m_max']

    weath_code = {'0': 'Clear sky', '1': 'Mainly clear', '2': 'Partly cloudy', '3': 'Overcast clouds',
                  '45': 'Fog', '48': 'Depositing rime fog', '51': 'Drizzle light rain',
                  '53': 'Drizzle moderate rain', '55': 'Dense intensity', '56': 'Light Freezing Drizzle',
                  '57': 'Dense intensity Freezing Drizzle', '61': 'Slight rain', '63': 'Moderate rain',
                  '65': 'Heavy intensity rain', '66': 'Light Freezing Rain', '67': 'Heavy intensity Freezing Rain',
                  '71': 'Slight snow fall', '73': 'Moderate snow fall', '75': 'Heavy intensity snow fall',
                  '77': 'Snow grains', '80': 'Slight Rain showers', '81': 'Moderate rain showers', '82': 'Violent rain showers',
                  '85': 'Slight Snow showers', '86': 'Heavy Snow showers', '95': 'Thunderstorm: Slight or moderate',
                  '96': 'Thunderstorm with slight hail', '99': 'Thunderstorm with heavy hail'}
    for i in range(len(dates)):
        output += "\n\n⌚ On {},\n\t🌡 Max temp: {} ℃,\n\t🌡 Min temp: {} ℃\n\t⛅ It will be: {}.\n".format(pd.Timestamp(dates[i]).day_name(), temp_max[i], temp_min[i], weath_code[str(summary[i])])
    return output
