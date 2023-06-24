import requests
import json
import sys
import os
from dotenv import load_dotenv
import argparse
import datetime
def get_coordinates(city):
    api_key=os.getenv("OPENCAGE_API_KEY")
    results = requests.get(f"https://api.opencagedata.com/geocode/v1/json?q={city}&key={api_key}").json()
    if results:
        lat=results['results'][0]['geometry']['lat']
        lon=results['results'][0]['geometry']['lng']
        print(lat, lon)
        return lat, lon
    else:
        print("Error")
        sys.exit()

load_dotenv()
api_key=os.getenv("WEATHER_API_KEY")
parser = argparse.ArgumentParser(description='Get weather for a city')
parser.add_argument('city', metavar='city', type=str, nargs='+',
                    help='the city to get the weather for')
args = parser.parse_args()
city = args.city[0]
print(f"Getting weather for {city}")
lat, lon = get_coordinates(city)
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
response = requests.get(url)
if response.status_code != 200:
    print(response.status_code)
    print("Sorry, that city was not found")
    sys.exit()
data = json.loads(response.text)
print(f"The weather in {city} is {data['weather'][0]['description']}")
print(f"The current temperature is {data['main']['temp']} degrees Fahrenheit")
print(f"Temperature feels like {data['main']['feels_like']} degrees Fahrenheit")
print(f"Today's temperature ranges from {data['main']['temp_min']} to {data['main']['temp_max']} degrees Fahrenheit")
print(f"Enjoy the sunrise at {datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Expect the sunset at {datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')}")
print(f"The current wind speed is {data['wind']['speed']} miles per hour from the {data['wind']['deg']} degrees direction")
print(f"The current humidity is {data['main']['humidity']}%")

