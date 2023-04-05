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
#### Core algorithm and code snippet 
- The core algorithm for this application is based on tokenizing the sentences and identifying the GPE - Geopolitical Entity and DATE - Date Entity.

![code snippet2](https://user-images.githubusercontent.com/72982296/230152666-4e538cf6-f752-4925-a1b3-0edabf337fe4.png)

- Another core algorithm is listing expected phrases to be used when someone asking for weather information and compare their similarity with the requests from user at predefined min value.

![code snippet](https://user-images.githubusercontent.com/72982296/230152897-8aec515d-714d-4ee5-b3ec-9140ce0e9381.png)


#### Inspiration and Story behind CForecast
It is known that ChatGPT is the current hot topic in the world of machine learning. It also inspired me to be inclined toward machine learning, and then I decided to develop a Chatbot-based application that operates like ChatGPT but with a single scope: weather. While thinking of this, the Holberton School, where I am attending a Full-stack Software Engineering class, asked us to do a portfolio project as a partial requirement to accomplish the foundation. Following this, I summited the proposal to the school; and it got approved. It was the birth of CForecast, and I started to work on this project with commitment.
#### Summary
![web_architecture (1)](https://user-images.githubusercontent.com/72982296/230151477-bf769058-49d8-481b-b4de-4159fb857711.png)
For the front end, I used the Telegram bot; and for back-end development, I used Python programming language. At the back end, I used many libraries such as pyTelegramBotAPI, spaCy, geopy, request, pandas, and so on to integrate with the Telegram bot, process the natural language and serve the user with weather data of a given city. And I used OpenWeatherMap API and Open-Metro as weather data sources.

CForecast has three main features.
- Feature: Current weather forecasting.
- Non-feature: The user uses the most popular chat application, Telegram, to access the CForecast features
- Feature: Upcoming n-days forecasting for nearly 16 days and not more than.
- Feature: Retrieves the archive of historical weather data of a given city to back 1940s.
#### Technical challenges
I thought OpenWeather was a free API, so I decided to work with it in my project’s early stages. However, OpenWeather is only free with the API to forecast the current weather conditions. So, I was obligated to search for free API; and I got an API provider named Open-metro that can do the forecasts for the next n consecutive days with its API integration, including historical data.

Then I started to integrate it with the telegram bot through pyTelegramBot API. However, I found it very difficult and time-consuming. I am obligated to read the whole documentation of the Open-Metro. And this let me have a basic understanding of the Open-Metro API, which is free for non-commercial users. Following this, I started to re-organize my implementation and rewrite it to meet the requirements listed in the user story. The task was as challenging as I expected. This was because I was restricted by the deadline and time. So I decided to do the easy thing first; to complete the portfolio project within the given period.

I did it. I have completed the CForecast portfolio project as an application that can function in what was listed in the user story, forecasting upcoming, current, and historical archives of a given city.
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
