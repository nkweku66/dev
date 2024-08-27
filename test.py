from pprint import pprint
import requests
import os
from dotenv import load_dotenv

load_dotenv()
weather_api = os.getenv('OWM_KEY')

r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=London&APPID={weather_api}')
details = r.json()
weather = details["weather"]
# weather_name = weather[2]
# weather_description = weather[4]

# print(f"There is a lot of {weather_name} and the weather has {weather_description}")
print(details["weather"])
