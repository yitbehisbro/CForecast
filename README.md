## Project Name    
The project's name is <code>CForcast</code> where C stands for Current. Its full name reads "Current and Forecast Weather of The Cities in The Globe". <code>CForecast</code> helps researchers, agricultural experts, merchants, farmers, travelers, and others to know the historical, current, or upcoming n days weather of a given city by using a natural language: English.

## Introduction
CForecast is a Chatbot-based current, upcoming, and historical weather forecasting application. It uses the Telegram bot as a chatting interface and the pyTelegramBotAPI library of Python as a back-end of the application. The weather data is accessed from OpenWeather and Open-metro through API and without API (Open-metro is free for non-commercial purposes without API). 

- A link to CForecast <a href="https://t.me/CForecastBot" target="_blank" >Telegram bot</a>  
- My LinkedIn Profile <a href="https://www.linkedin.com/in/yitbewendimu" target="_blank" >Yitbarek Wendimu</a>
#### Technology and Architecture
The technology I used for this portfolio project are:
- Machine learning: I used this to train the model and let it to understand the natural language and respond the weather data. For this purpose I used spaCy library and its package for English language.
- Web API: I used API to integrate with Telegram bot and to access historical, current or upcoming weather data. For this purpose I used Telegram bot API and OpenWeatherMap API as well as Open-Metro API.
- Programming language I used for this implementation was a Python.


## Installation
- Clone the repo: <code>git clone https://github.com/yitbehisbro/CForecast.git</code>
- Change directory to CForecast: <code>cd CForecast</cd></code>
- Install the following libraries:
<pre>
<code>yitbe@ubuntu:~$ pip install pyTelegramBotAPI</code>
<code>yitbe@ubuntu:~$ pip install -U pip setuptools wheel</code>
<code>yitbe@ubuntu:~$ pip install -U spacy</code>
<code>yitbe@ubuntu:~$ python -m spacy download en_core_web_sm</code>
<code>yitbe@ubuntu:~$ python -m spacy download en_core_web_md</code>
<code>yitbe@ubuntu:~$ pip install requests</code>
<code>yitbe@ubuntu:~$ pip install geopy</code>
<code>yitbe@ubuntu:~$ pip install pandas</code>
<code>yitbe@ubuntu:~$ pip install dateparser</code>
</pre>
- Add the following envirnomental variable:
<pre>
<code>yitbe@ubuntu:~$ export API_TOKEN="YOUR OpenWeather API"</code>
<code>yitbe@ubuntu:~$ export TOKEN="YOUR TELEGRAM BOT API TOKEN"</code>
</pre>
- Run the <code>cforecast_bot.py</code>:
<pre>
<code>yitbe@ubuntu:~$ python3 cforecast_bot.py</code>
</pre>
- Now you can chat from the Telegram bot

## Usage
- Download (<a href="https://apps.apple.com/app/telegram-messenger/id686449807" target="_blank">iPhone/iPad</a> or <a href="https://telegram.org/android" target="_blank">Android</a> or <a href="https://desktop.telegram.org/" target="_blank">Desktop</a> or <a href="https://macos.telegram.org/" target="_blank">macOS</a>) and Install the Telegram Application
- Use <a href="https://t.me/CForecastBot" target="_blank">this link</a> to open the CForecast bot
- Then start the bot by clicking the button <code>Start</code> which is at the very bottom of the app

![start_bot](https://user-images.githubusercontent.com/72982296/230132415-0bccc50d-cb2c-469e-af01-318b09a2155e.png)

- Then type something like <code>Tell me the current weather in Addis Abeba</code> and hit ENTER (The output might look like the following)

![sample(croped)](https://user-images.githubusercontent.com/72982296/230132817-4f00fa29-7e63-4f8b-beb4-ea741f5fcc3d.png)

- You can ask for consecutive n-days forecast for a particular city by just typing something like <code>Tell me the upcoming 6 days weather forecast in Hawassa</code> (The output will look like)

![sample2](https://user-images.githubusercontent.com/72982296/230138978-6131e1f9-cfee-4394-abe4-4df7ce5fbdb0.png)

- You can also ask for historical weather data by typing something like <code>Tell me the historical weather data of London from 14th March 2011 to 17th March 2011</code> (But here the <code>start date</code> and <code>end date</code> as well as the <code>city name</code> mandatory)

![sample3](https://user-images.githubusercontent.com/72982296/230134313-7e3bc2fa-6224-4c57-83d9-66fa33bc491d.png)

## Contributing

<code>CForecast</code> helps researchers, agricultural experts, merchants, farmers, travelers, and others to know the historical, current, or upcoming n days weather of a given city by using a natural language: English.

## Related projects

- I found something named <a href="https://medium.com/weatherbot/telegram-bot-for-weather-report-f688ada85b93" target="_blank"> WeatherBot </a>, from <a href="https://medium.com/" target="_blank">Medium</a> blog, which is a Telegram bot based weather forcasting application. It prompts the user to enter the name of city or location from google map API.
- Also found another one from GitHub named <a href="https://github.com/mustafababil/Telegram-Weather-Bot" target="_blank">Telegram Weather Bot</a>, which has also nearly the same feature as of the first one.

Both of them has no idea about machine learning and natural language processing which means they are not chatbot based and not use natural language to get the current, upcoming and historical weather data.

## Licensing

You are free to use, contribute to or change <code>CForecast</code>. However, I ask you to give a little credit and apprication for my effort. For more detail read [LICENSE](https://github.com/yitbehisbro/CForecast/blob/main/LICENSE).
