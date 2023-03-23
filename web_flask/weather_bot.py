#!/usr/bin/python3
import requests
import spacy
import sys
import telebot
import random
from model.forecast7days import refine_data


bot = telebot.TeleBot("6008131177:AAF05_P4Ft1Olli0AC1CWLW2pKcQEXFexz4")

api_key = "fc083a590244ec5531e6753618ba21fd"
nlp = spacy.load("en_core_web_md")
min = max = feels = temp = None


def get_weather(city_name):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)
    response = requests.get(api_url)
    response_dict = response.json()
    try:
        weather = response_dict["weather"][0]["description"]
        min = response_dict["main"]["temp_min"]
        max = response_dict["main"]["temp_max"]
        feels = response_dict["main"]["feels_like"]
        temp = response_dict["main"]["temp"]

        if response.status_code == 200:
            # return weather
            # weath = "\033[1;37m" + weather
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
        for i in range(len(weather)):
            # if weather.similarity(statement) >= min_similarity:
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
                    # text2 = ".\nMin: {} Max: {}\nFeels like: {}.".format(min, max, feels)
                    return text
                else:
                    return "Something went wrong."
            else:
                return "Sorry I don't understand that. Please rephrase your statement."
    except Exception:
        print("Too many requests!")


@bot.message_handler(commands=['start', 'historical', 'help'])
def send_welcome(message):
    if message.text == "/help":
        bot.reply_to(message, "Hello @{}!\n{}".format(message.from_user.username,
                                                      "We are in hurry preparing a manual. Thank you for your patience."))
    elif message.text == "/historical":
        bot.reply_to(message, "Hello @{}!\n{}".format(message.from_user.username,
            "We are in hurry developing the integration. Thank you for your patience."))
    else:
        bot.reply_to(message, "Howdy, how are you doing?")
        # bot.reply_to(message, message)


@bot.message_handler(func=lambda message: True)
def answer(message):
    """Response to the telegram bot requests"""

    gratitude = [nlp("Thank you"), nlp("Thanks"), nlp("hats off"), nlp("hats off to you")]
    statement = nlp(message.text)
    for ent in statement.ents:
        if ent.label_ == "GPE":  # GeoPolitical Entity
        # print(ent.text)
            response = get_weather(ent.text)  # Gets the weather directly by the city name
            bot.reply_to(message, "Hello @{}!\nIn {}, {}\n\nIn upcomming 7 days:{}".format(message.from_user.username, ent.text, response, refine_data(ent.text)))
            exit()
    min_similarity = 0.75
    rand = random.randint(0, 5)
    respo = ["My pleasure!", "You are welcome!", "Never mind!", "It's okay", "Thank you too!", "Oh, no!"]
    for i in range(len(gratitude)):
        if gratitude[i].similarity(statement) >= min_similarity:
            bot.reply_to(message, respo[rand])
            exit()

    response = chatbot(message.text)
    bot.reply_to(message, "Hello @{}!\n{}".format(message.from_user.username, response))


if __name__ == "__main__":
    bot.infinity_polling()
