## Project Name    
The project's name is <code>CForcast</code> where C stands for Current. Its full name reads "Current and Forecast Weather of The Cities in The Globe". 

## Introduction
CForecast is a Chatbot-based current, upcoming, and historical weather forecasting application.. It uses the Telegram bot as a chatting interface and the pyTelegramBotAPI library of Python as a back-end of the application. The weather data is accessed from OpenWeather and Open-metro through API and without API (Open-metro is free for non-commercial purposes without API).

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
