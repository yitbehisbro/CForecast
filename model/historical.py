from .forecast_n_days import coordinate, weather_code
import requests
import spacy
import dateparser
import pandas as pd

nlp = spacy.load("en_core_web_sm")


def get_time(dates):
    """ Get the time from the date time """
    if dates is None:
        return None
    time = dateparser.parse(dates)
    time = pd.Timestamp(time, tz='UTC')
    time = str(time).split(" ")
    time = time[1].split("+")
    return time[0]


def get_historical_data(city=None, start_date=None, end_date=None):
    """ Get data from the web API """
    coord = coordinate(city)
    url = "https://archive-api.open-meteo.com/v1/archive?latitude={}&longitude={}&start_date={}&end_date={}" \
          "&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset," \
          "rain_sum&timezone=Africa%2FCairo".format(coord["lat"], coord["lon"], start_date, end_date)
    res = requests.get(url)
    text = ""
    result = res.json()
    time = result['daily']['time']
    weathercode = result['daily']['weathercode']
    rain_sum = result['daily']['rain_sum']
    temp_max = result['daily']['temperature_2m_max']
    temp_min = result['daily']['temperature_2m_min']
    sunrise = result['daily']['sunrise']
    sunset = result['daily']['sunset']
    for i in range(len(time)):
        text += "\n⌚ On {} (Week {}):\n\n\t🌞\t  Day name: {}\n\t⛅ \t Weather: {}\n\t🌧 \t Rain: {} mm\n\t🌡 \t " \
                "Max temp: {} ℃\n\t🌡 \t Min temp: {} ℃\n\t🌘\t  Sun rose: {} UTC\n\t🌒\t  Sun set: {} " \
                "UTC\n\n".format(time[i], pd.Timestamp(time[i]).week, pd.Timestamp(time[i]).day_name(),
                                 weather_code(weathercode[i]), rain_sum[i], temp_max[i], temp_min[i],
                                 get_time(sunrise[i])[:-3], get_time(sunset[i])[:-3])
    return text


def return_historical_data(statement):
    """ Identify the date and GPE entity """
    dates = []
    city = ""
    statement = nlp(statement)
    for ent in statement.ents:
        if ent.label_ == 'DATE':  # Date Entity
            dates.append(ent.text)
        if ent.label_ == 'GPE':  # Geopolitical entity
            city = ent.text
    print(dates)
    print(statement)
    try:
        dates = dates[0].split("to")
        print(dates)
        start_date = dateparser.parse(dates[0])
        end_date = dateparser.parse(dates[1])
        start_date = str(start_date).split(" ")
        start_date = start_date[0]
        end_date = str(end_date).split(" ")
        end_date = end_date[0]
        metadata = {"city": city, "start_date": start_date, "end_date": end_date}
        if metadata["city"] and metadata["start_date"] and metadata["end_date"] is None:
            return "Minimum requirement not satisfied!"
        return get_historical_data(metadata["city"], metadata["start_date"], metadata["end_date"])
    except Exception:
        return 400


"""if __name__ == "__main__":
    print(historical("Hawassa", "2023-02-14", "2023-02-15"))
    print(return_historical_data("Historical data from 24th June 2022 to 24th March 2023 in Hawassa!"))
    print("Start date is: {}.".format(metadata['start_date']))
    print(return_historical_data("Data from 13/04/2012 to 14/04/2013 in Hawassa!"))"""
