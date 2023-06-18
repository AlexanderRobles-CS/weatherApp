class User:
    def __init__(self):
        self.location = self.getLocation()
        self.userInterface = self.UserInterface()
    
    def getLocation(self):           # do this later
        return "San Francisco, CA"
    
    def UserInterface(self):
        print(f"Good Morning, the time is 8:00 AM.")
        print(f"The weather today in {self.location} is sunny and 75 degrees.")
    
    def getUserInput(self):
        while True:
            userInput = input(" ")
            if userInput == "quit":
                break
            else:
                print(userInput)

