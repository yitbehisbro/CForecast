## Project Name    
The project's name is <code>CForcast</code> where C stands for Current. Its full name reads "Current and Forecast Weather of The Cities in The Globe". 

## Introduction
CForecast is a Chatbot-based current, upcoming, and historical weather forecasting application. It uses the Telegram bot as a chatting interface and the pyTelegramBotAPI library of Python as a back-end of the application. The weather data is accessed from OpenWeather and Open-metro through API and without API (Open-metro is free for non-commercial purposes without API).

- A link to CForecast <a href="https://t.me/CForecastBot" target="_blank" >Telegram bot</a>  
- My LinkedIn Profile <a href="https://www.linkedin.com/in/yitbewendimu" target="_blank" >Yitbarek Wendimu</a>

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

- You can ask for consecutive n-days forecast for a particular city by just typing something like <code>

- You can also ask for historical weather data by typing something like <code>Tell me the historical weather data of London from 14th March 2011 to 17th March 2011</code> (But here the <code>start date</code> and <code>end date</code> as well as the <code>city name</code> mandatory)

![sample3](https://user-images.githubusercontent.com/72982296/230134313-7e3bc2fa-6224-4c57-83d9-66fa33bc491d.png)

