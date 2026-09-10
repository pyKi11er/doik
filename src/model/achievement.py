from dataclasses import dataclass
from time import datetime

#A class for achievements that the user can unlock based on their progress in the app.
# or for streak milestones
@dataclass
class Achievement:
    def __init__(self):
        self.__achievement_name = ""
        self.__achievement_description = ""
        self.__achievement_id = None
        self.__achievement_date = datetime.now()
        self.__streak_milestone = None

    def getAchievementName(self):
        return self.__achievement_name

    def getAchievementDescription(self):
        return self.__achievement_description

    def getAchievementId(self):
        return self.__achievement_id

    def getAchievementDate(self):
        return self.__achievement_date

    def getStreakMilestone(self):
        return self.__streak_milestone
    
    def setAchievementName(self, achievement_name: str):
        self.__achievement_name = achievement_name

    def setAchievementDescription(self, achievement_description: str):
        self.__achievement_description = achievement_description

    def setAchievementId(self, achievement_id: int):
        self.__achievement_id = achievement_id

    def setAchievementDate(self, achievement_date: datetime):
        self.__achievement_date = achievement_date

    def setStreakMilestone(self, streak_milestone: int):
        self.__streak_milestone = streak_milestone
