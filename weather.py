from dotenv import load_dotenv
from pprint import pprint 
import requests
import os

load_dotenv()

def get_current_weather(city="Detroit"):
    
    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__": 
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")
    
        #check for empty stings or stings with empty spaces.
    if not bool(city.strip()):
        city = "Detroit"

    weather_data = get_current_weather(city)
    print("\n")
    print(weather_data)


