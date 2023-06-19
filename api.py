import requests

class API:
    def __init__(self, location):
        self.BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        self.API_KEY = open("api_key","r").read()
        self.CITY = location
        self.url = self.BASE_URL + "appid=" + self.API_KEY + "&q=" + self.CITY
        self.response = requests.get(self.url).json()
        self.forecastURL = None
        self.forecastResponse = None
        self.weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def getForecast(self):
        self.forecastURL = "https://api.openweathermap.org/data/2.5/forecast?q=" + self.CITY + "&appid=" + self.API_KEY
        self.forecastResponse = requests.get(self.forecastURL).json()
        # print(self.forecastResponse)

    def forecastInterface(self, convert):
        weather_data = self.forecastResponse
        forecast_list = weather_data['list']

        daily_forecasts = {}

        for forecast in forecast_list:
            dt_txt = forecast['dt_txt']
            date = dt_txt.split()[0]
            if date not in daily_forecasts:
                temperature = forecast['main']['temp']
                feels_like = forecast['main']['feels_like']
                description = forecast['weather'][0]['description']
                daily_forecasts[date] = {
                    'Temperature': temperature,
                    'Feels Like': feels_like,
                    'Description': description
                }

        # Print the daily forecasts
        for date, forecast in daily_forecasts.items():
            print(f"Date: {date}")
            print(f"Temperature: {convert.kelvinToFahrenheit(forecast['Temperature'])} degrees F")
            print(f"Description: {forecast['Description']}")
            print("------")