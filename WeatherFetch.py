import requests
import random
import os
from dotenv import load_dotenv

#Super simple weather app that fetches weather data and the name of the location when given coordinates
#Uses the OpenWeatherMap API

def fetch_weather_data(lat,lon, API_key):

    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric')
    data = response.json()
    weather = data["weather"][0]["main"]
    description = data["weather"][0]["description"]
    temp=data["main"]["temp"]
    humidity=data["main"]["humidity"]
    print(f"The location is currently experiencing {weather} and can be described as having {description}")
    print(f"The local temperature is {temp} Celcius degrees with a humidity level of {humidity}%")


def reverse_geocode(lat,lon, API_key): #To get the name of this place

    response = requests.get(f'http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit={1}&appid={API_key}')
    data = response.json()
    if (data == []):
        print("This place is not known as a major area and cannot be found by reverse geocoding")
    else:
        name = data[0]["name"]
        print(f"This place is known as {name}")


def main():

    #Hong Kong Island coordinates
    #lat = 22.2588
    #lon = 114.1911

    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    
    print("Welcome to our weather app! If you would like to know more about the weather in any part of the world\nEnter the latitudes and longitudes or just press Enter for a random location")
    lat = input("Please input a float latitude value (from -90 to 90)")
    lon = input("Please input a float latitude value (from -180 to 180)")
    print("\n\n")

    if (lat=="" or lon==""):
        lat = random.randint(-90,90)
        lon = random.randint(-180,180)
        reverse_geocode(lat,lon, API_KEY) 
        fetch_weather_data(lat,lon, API_KEY)
    else:
        reverse_geocode(lat,lon, API_KEY)
        fetch_weather_data(lat,lon, API_KEY)

if __name__ == "__main__":
    main()