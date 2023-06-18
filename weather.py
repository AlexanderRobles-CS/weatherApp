from user import User

class Weather:
    def __init__(self,user):
        self.user = user
        self.location = self.user.getLocation()
        self.weather = self.getWeather()

    def getWeather(self):
        # make API call to get weather
        return "sunny and 75 degrees"