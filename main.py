import argparse
import pyfiglet
import json
import requests
from simple_chalk import chalk

API_KEY="b4de947058ed470c490b41beed0c8b20"

BASE_URL="https://api.openweathermap.org/data/2.5/weather"

WEATHER_ICONS = {
    # day icons
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",
    # night icons
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫",
}
#by using argparse crete the argument for country"country" and parse that arguments to the terminal
parser=argparse.ArgumentParser(description="check the weather for a certain country/city")
parser.add_argument("country",help="the country/city to check the weather for")
args=parser.parse_args()

#base url setting
url=f"{BASE_URL}?q={args.country}&appid={API_KEY}&units=metric"

#make api request and response
response=requests.get(url)
if response.status_code!=200:
    print(chalk.red("Errror: Unable to  retrive weather information "))

#parsing the json request
data=response.json()

#get information from json
temperature=data["main"]["temp"]
feels_like=data["main"]["feels_like"]
#description=data["weather"][0]["icon"]
icon = data["weather"][0]["icon"]
city=data["name"]
country=data["sys"]["country"]

#construct the output with weqather icon
weather_icons=WEATHER_ICONS.get(icon,"")
output=f"{pyfiglet.figlet_format(city)},{country}\n\n"
output+=f"{weather_icons} {icon}"
output+=f"temperature : {temperature}°C"
output+=f"feels_like : {feels_like}°C"

print(chalk.green(output))