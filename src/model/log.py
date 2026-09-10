from dataclasses import dataclass
from time import datetime

# A daily log class for logging sleep hours, meals, and mood. 
# This will be used to determine the xp contribution for the questline and category
# in the future, also will affect stamina and focus
@dataclass
class Log:
    def __init__(self):
        self.__log_id = None
        self.__ref_to_character = None
        self.__timestamp = datetime.now()
        self.__sleep_hours = 0
        self.__meal = None
        self.__mood = None

    def getLogId(self):
        return self.__log_id

    def getRefToCharacter(self):
        return self.__ref_to_character
    
    def getTimestamp(self):
        return self.__timestamp

    def getSleepHours(self):
        return self.__sleep_hours

    def getMeal(self):
        return self.__meal

    def getMood(self):
        return self.__mood

    def setLogId(self, log_id: int):
        self.__log_id = log_id

    def setRefToCharacter(self, character):
        self.__ref_to_character = character

    def setSleepHours(self, sleep_hours: int):
        self.__sleep_hours = sleep_hours

    def setMeal(self, meal):
        self.__meal = meal

    def setMood(self, mood):
        self.__mood = mood
