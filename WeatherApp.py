import requests
import json
import sys
import os
from dotenv import load_dotenv
import argparse
import datetime
def get_coordinates(city):
    api_key=os.getenv("OPENCAGE_API_KEY")  # opencage API key is the api key for opencage geocoder API
    #Opencage is a geocoding API that converts city names to lat/lon coordinates
    results = requests.get(f"https://api.opencagedata.com/geocode/v1/json?q={city}&key={api_key}").json() # json() converts the response to a dictionary
    if results:
        lat=results['results'][0]['geometry']['lat']# results is a dictionary, and the 'results' key has a list of dictionaries, and the first item in the list has a 'geometry' key with a 'lat' key
        lon=results['results'][0]['geometry']['lng']# similarly, the 'lng' key has the longitude
        print(lat, lon)
        return lat, lon
    else:
        print("Error")
        sys.exit()

load_dotenv() # load environment variables from .env file
api_key=os.getenv("WEATHER_API_KEY") #weather API key is the api key for openweathermap
parser = argparse.ArgumentParser(description='Get weather for a city') # argparse is a module that allows you to pass arguments to your program
parser.add_argument('city', metavar='city', type=str, nargs='+',
                    help='the city to get the weather for')# nargs='+' means that you can pass multiple arguments to the program 
args = parser.parse_args() # add_argument() adds an argument to the parser, description is the help text that is displayed when you run the program with the -h flag
# parse_args() parses the arguments passed to the program and returns a Namespace object
city = args.city[0]
print(f"Getting weather for {city}")
lat, lon = get_coordinates(city)
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}" # the url for the weather API endpoint with the lat and lon coordinates
response = requests.get(url)
if response.status_code != 200:  # if the response status code is not 200, then there was an error
    print(response.status_code)
    print("Sorry, that city was not found")
    sys.exit()
data = json.loads(response.text)  # convert the response to a dictionary
print(f"The weather in {city} is {data['weather'][0]['description']}")
print(f"The current temperature is {data['main']['temp']} degrees Fahrenheit")
print(f"Temperature feels like {data['main']['feels_like']} degrees Fahrenheit")
print(f"Today's temperature ranges from {data['main']['temp_min']} to {data['main']['temp_max']} degrees Fahrenheit")
print(f"Enjoy the sunrise at {datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Expect the sunset at {datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')}")
print(f"The current wind speed is {data['wind']['speed']} miles per hour from the {data['wind']['deg']} degrees direction")
print(f"The current humidity is {data['main']['humidity']}%")

