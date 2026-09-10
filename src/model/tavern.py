from datetime import datetime

class Tavern:
    def __init__(self):
        self.__tavern_offer_id = None
        self.__timestamp = datetime.now()
        self.__pool_of_choices = []
        self.__context_state = None  # time of day, remaining stamina, remaining
                                      # focus, recent completions - was ambiguously
                                      # named "state" and typed as a bare string
        self.__final_choices = []
        self.__explanation = ""
        self.__reward = ""  # flavor/response text on accept, e.g. "The keeper nods
                             # approvingly" - NOT numeric, actual XP/gold lives on Quest
        self.__mood = None

    def getTavernOfferId(self):
        return self.__tavern_offer_id

    def getTimestamp(self):
        return self.__timestamp

    def getPoolOfChoices(self):
        return self.__pool_of_choices.copy()

    def getContextState(self):
        return self.__context_state

    def getFinalChoices(self):
        return self.__final_choices.copy()

    def getExplanation(self):
        return self.__explanation

    def getReward(self):
        return self.__reward

    def getMood(self):
        return self.__mood

    def setTavernOfferId(self, tavern_offer_id: int):
        self.__tavern_offer_id = tavern_offer_id

    def setPoolOfChoices(self, pool_of_choices):
        for i in pool_of_choices:
            self.__pool_of_choices.append(i)

    def setContextState(self, context_state):
        self.__context_state = context_state

    def setFinalChoices(self, final_choices):
        for i in final_choices:
            self.__final_choices.append(i)

    def setExplanation(self, explanation):
        self.__explanation = explanation

    def setReward(self, reward: str):
        self.__reward = reward

    def setMood(self, mood):
        self.__mood = mood