from api import API

class User:
    def __init__(self):
        self.getUserInput()
    
    def userInterface(self, api):
        print(f"The weather in {api.CITY} is {api.response['weather'][0]['description']}.")
        print(f"With a current temperature of {self.kelvinToFahrenheit(api.response['main']['temp'])} degrees Fahrenheit.")
    
    def kelvinToFahrenheit(self, kelvin):
        farenheit = (kelvin - 273.15) * 9/5 + 32
        formattedFarenheit = "{:.2f}".format(farenheit)
        return formattedFarenheit
    
    def getUserInput(self):
        print("Type 'quit' to exit the program.")
        while True:
            location = input("Where would you like to get the weather from? \n")
            userInput = input("Type 'Day/Week for the weather in your desired location. \n").lower()
            
            if userInput == 'day':
                api = API(location)
                self.userInterface(api)

            if userInput == "week":
                print(f"Here is the forecast for the next 5 days in {location}")
                api = API(location)
                api.getForecast()
                api.forecastInterface(self)

            elif userInput == "quit":
                break

