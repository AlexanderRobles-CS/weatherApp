from user import User
from weather import Weather

import datetime as dt
import requests

def main():
    user = User()
    weather = Weather(user)
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = open("api_key","r").read()
    CITY = "San Francisco"

    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

    response = requests.get(url).json()

    print(response)

if __name__ == "__main__":
    main()
