from sys import datetime
from dataclasses import dataclass

@dataclass
class Quest:
    def __init__(self):
        self.__title = ""
        self.__type = None
        self.__reward_xp = calculateRewardXP()
        self.__completion_time = calculateCompletionTime()
        self.__stamina_cost = calculateStaminaCost()
        self.__focus_cost = calculateFocusCost()
        self.__category = getCategory()
        self.__reward_tier = calculateRewardTier()
        self.__emotional_weight = calculateEmotionalWeight()
        self.__parent_quest = None
        self.__decay_rate = calculateDecayRate()
        self.__state = 0
        self.__time_of_creation = datetime.now()
        self.__time_completion = None
        self.__recurring = False


    def getTitle(self):
        return self.__title

    def getType(self):
        return self.__type

    def getRewardXP(self):
        return self.__reward_xp

    def getCompletionTime(self):
        return self.__completion_time

    def getStaminaCost(self):
        return self.__stamina_cost

    def getFocusCost(self):
        return self.__focus_cost

    def getCategory(self):
        return self.__category

    def getRewardTier(self):
        return self.__reward_tier

    def getEmotionalWeight(self):
        return self.__emotional_weight

    def getParentQuest(self):
        return self.__parent_quest

    def getDecayRate(self):
        return self.__decay_rate

    def getState(self):
        return self.__state

    def getTimeOfCreation(self):
        return self.__time_of_creation

    def getTimeCompletion(self):
        return self.__time_completion

    def isRecurring(self):
        return self.__recurring

    def setTitle(self, title: str):
        self.__title = title

    def setType(self, type):
        self.__type = type

    def setRewardXP(self, reward_xp: int):
        self.__reward_xp = reward_xp

    def setCompletionTime(self, completion_time):
        self.__completion_time = completion_time

    def setStaminaCost(self, stamina_cost: int):
        self.__stamina_cost = stamina_cost

    def setFocusCost(self, focus_cost: int):
        self.__focus_cost = focus_cost

    def setCategory(self, category):
        self.__category = category

    def setRewardTier(self, reward_tier):
        self.__reward_tier = reward_tier

    def setEmotionalWeight(self, emotional_weight):
        self.__emotional_weight = emotional_weight

    def setParentQuest(self, parent_quest):
        self.__parent_quest = parent_quest

    def setDecayRate(self, decay_rate):
        self.__decay_rate = decay_rate

    def setState(self, state: int):
        self.__state = state

    def setTimeOfCompletion(self, time_of_completion):
        self.__time_completion = time_of_completion

    def setRecurring(self, recurring: bool):
        self.__recurring = recurring


    def calculateRewardXP(self):
        ...

    def calculateCompletionTime(self):
        ...

    def calculateStaminaCost(self):
        ...

    def calculateFocusCost(self):
        ...

    def calculateRewardTier(self):
        ...

    def calculateEmotionalWeight(self):
        ...

    def calculateDecayRate(self):
        ...

    


    

    