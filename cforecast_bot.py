#!/usr/bin/python3
import requests
import spacy
import telebot
import random
from model.forecast_n_days import refine_data
from model.historical import return_historical_data

api_key = os.environ['API_TOKEN']
bot = telebot.TeleBot(os.environ['TOKEN'])
nlp = spacy.load("en_core_web_md")
min = max = feels = temp = None

def get_weather(city_name):
    """Returns the weather data of a city unless otherwise error messages"""
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)
    response = requests.get(api_url)
    response_dict = response.json()
    try:
        weather = response_dict["weather"][0]["description"]
        min = response_dict["main"]["temp_min"]
        max = response_dict["main"]["temp_max"]
        feels = response_dict["main"]["feels_like"]

        if response.status_code == 200:
            text = "the current weather is: {}.".format(weather)
            text2 = "\n\n⛅ Temperature in the city:\n\n\t🌡 Min: {} ℃\n\t🌡 Max: {} ℃\n\n\t⛅ Feels like: {} ℃.".format(
                round(int(min) - 273.15, 2),
                round(int(max) - 273.15, 2), round(int(feels) - 273.15, 2))
            if round(int(feels) - 273.15, 2) < 10:
                return text + text2 + "\n\n👨‍✈️\t\t\"Before going outside, please make sure you dress very well.\"\n"
            return text + text2
        else:
            print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
            # return None
    except Exception:
        print("Unknown city name: ({}).".format(city_name))


def chatbot(statement):
    """Chatbots reply for weather and similar requests"""
    weather = [nlp("Current weather in London"),
               nlp("What is the current weather in London"),
               nlp("about rain in London"),
               nlp("the weather condition bad in London"),
               nlp("London"),
               nlp("hot weather"),
               nlp("cold weather")]
    statement = nlp(statement)
    min_similarity = 0.75
    try:
        city = ""
        for i in range(len(weather)):
            if weather[i].similarity(statement) >= min_similarity:
                for ent in statement.ents:
                    if ent.label_ == "GPE":  # GeoPolitical Entity
                        city = ent.text

                        break
                    else:
                        return "You need to tell me a city to check."

                city_weather = get_weather(city)
                if city_weather is not None:
                    text = "In " + city + ", " + city_weather
                    return text
                else:
                    return "Something went wrong."
            else:
                return "Sorry I don't understand that. Please rephrase your statement."
    except Exception:
        print("Too many requests!")


@bot.message_handler(commands=['start', 'historical', 'help'])
def send_welcome(message):
    """Sends reply to the command from the telegram bot"""
    if message.text == "/help":
        bot.reply_to(message, "Hello @{}!\n{}".format(message.from_user.username, "We are in hurry preparing a "
                                                                                  "manual. Thank you for your "
                                                                                  "patience."))
    elif message.text == "/historical":
        bot.reply_to(message, "Hello @{}!\n{}".format(message.from_user.username,
                                                      "To get the historical weather data correctly, please use these "
                                                      "like format of date. Example: '12nd April "
                                                      "2011 to 15th May 2011'.\nThank you!"))
    else:
        bot.reply_to(message, "Hello @{}!\nI am a CForecast bot assistant. How may I help you?".format(
            message.from_user.username))


@bot.message_handler(func=lambda message: True)
def answer(message):
    """Response to the telegram bot text based requests but not commands
        nlp: loading the NLP
        metadata: stores city and date data for further uses
        forecast_day: stores the number of forecasting day
        daysdata: stores data to be used for user defined days forecast
                Its purpose is to compare user input and variable stored at metadata['date']
        min_similarity: minimum similarity of the user inputted statement and model learning data
        rand: randomize numbers in 0 to 5 which used to respond for gratitude in different text in each reply
    """
    nlp1 = spacy.load("en_core_web_sm")
    metadata = {"city": [], "date": []}
    forecast_day = None
    daysdata = ["0 day", "1 day", "2 days", "3 days", "4 days", "5 days", "6 days", "7 days", "8 days",
                "9 days", "10 days", "11 days", "12 days", "13 days", "14 days", "15 days", "16 days"]
    daycmp = [nlp("16 days"), nlp("16 day"), nlp("160 day"), nlp("160 days"), nlp("1600 days"), nlp("16000 days")]

    """Respond to a gratitude from users"""
    gratitude = [nlp("Thank you"), nlp("Thanks"), nlp("hats off"), nlp("hats off to you")]
    statement = nlp(message.text)
    min_similarity = 0.75
    rand = random.randint(0, 5)
    respo = ["My pleasure!", "You are welcome!", "Never mind!", "It's okay", "Thank you too!", "Oh, no!"]
    for i in range(len(gratitude)):
        if gratitude[i].similarity(statement) >= min_similarity:
            bot.reply_to(message, respo[rand])
            exit()
    """End of responding to a gratitude from users"""

    """Check for date and GeoPolitical Entity which is city in my case"""
    statement = nlp1(message.text)
    for ent in statement.ents:
        if ent.label_ == "GPE":  # GeoPolitical Entity
            metadata['city'].append(ent.text)
        if ent.label_ == "DATE":
            metadata['date'].append(ent.text)
    """End of looking for date and GPE from statements"""

    """Refines the date and got the day numeric value and setts it
    to forecast user defined number of days"""
    if len(metadata['date']) >= 1 and metadata['date'][0] in daysdata:
        numeric_day = str(metadata['date'][0]).split(" ")
        forecast_day = int(numeric_day[0])
        if forecast_day > 16:
            bot.reply_to(message, "Hello @{}!\nUnfortunately, I can not do a forecast for more than 16 days.\nSorry "
                                  "for that.".format(message.from_user.username))
            exit()
        if forecast_day <= 0:
            bot.reply_to(message, "Hello @{}!\nYou used an invalid day numbers so that I can not do a forecast for "
                                  "it. Sorry for that.".format(message.from_user.username))
            exit()
    """End of refining the numeric value of days"""

    """Responds for a historical or user defined number of days forecasting
    weather data requests"""
    if len(metadata['city']) >= 1 and len(metadata['date']) >= 1:
        print(metadata['date'][0])

        """Responds for historical weather data requests"""
        if metadata['date'][0] not in daysdata:
            """Responds for more than 16 days or invalid days number"""
            statement = nlp(metadata['date'][0])
            for i in range(len(daycmp)):
                if daycmp[i].similarity(statement) >= min_similarity:
                    numeric_day = str(metadata['date'][0]).split(" ")
                    forecast_day = int(numeric_day[0])
                    """For days greater than 16 days (responds)"""
                    if forecast_day > 16:
                        bot.reply_to(message,
                                     "Hello @{}!\nUnfortunately, I can not do a forecast for more than 16 days.\nSorry "
                                     "for that.".format(message.from_user.username))
                        exit()
                    """For days greater invalid days (responds)"""
                    if forecast_day <= 0:
                        bot.reply_to(message,
                                     "Hello @{}!\nYou used an invalid day numbers so that I can not do a forecast for "
                                     "it. Sorry for that.".format(message.from_user.username))
                        exit()
            results = return_historical_data(message.text)
            try:
                if results == 400:
                    bot.reply_to(message, "Hello @{}!\n{}".format(message.from_user.username, "Something went wrong. "
                                                                                              "We're working on it. "
                                                                                              "Meanwhile, "
                                                                                              "check if your date "
                                                                                              "format is right. Refer "
                                                                                              "at /historical"))
                    exit()
                bot.reply_to(message, "Hello @{}!\n\n⛄ Here is the historical weather data of {} from {} ⛄\n\n{}\nI "
                                      "hope this will help you!".format(message.from_user.username, metadata['city'][0],
                                                                        metadata['date'][0], results))
                exit()
            except Exception:
                bot.reply_to(message, "Hello @{}!\n{}".format(message.from_user.username, "Something went wrong! We "
                                                                                          "are working on "
                                                                                          "it.\nMeanwhile, "
                                                                                          "please check if you're "
                                                                                          "asking for more than 15 "
                                                                                          "days historical data, "
                                                                                          "which is beyond our "
                                                                                          "capacity or your date "
                                                                                          "format. Refer at "
                                                                                          "/historical"))
                exit()
        """End of historical data reply"""

        """Responds for user defined number of days weather forecasting"""
        if metadata['date'][0] in daysdata:
            print("Got it!")
            response = refine_data(forecast_day, metadata['city'][0])
            bot.reply_to(message, "Hello @{}!\nThe weather in {}, in upcoming {} days will be:\n\n{}".format(
                message.from_user.username, metadata['city'][0], forecast_day, response))
            exit()
        """End of user defined number of days forecast"""

    """End of replying to historical and user defined number of days weather forecasting"""

    """Responds for current weather data requests"""
    if len(metadata['city']) >= 1 and len(metadata['date']) == 0:
        # print("GOt it too!")
        response = get_weather(metadata['city'][0])  # Gets the weather directly by the city name
        bot.reply_to(message, "Hello @{}!\nIn {}, {}".format(message.from_user.username, metadata['city'][0], response))
        exit()
    """End of current weather data requests"""

    """Response to un-catchable user inputs or requests"""
    response = chatbot(message.text)
    bot.reply_to(message, "Hello @{}!\n{}".format(message.from_user.username, response))


if __name__ == "__main__":
    """ Loops the chatbot infinitely """
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
