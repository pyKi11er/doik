from dataclasses import dataclass

@dataclass
class Character:
    def __init__(self, stamina :int, focus : int):
        self.__name = ""
        self.__level = calculateLevel()
        self.__total_xp = 0
        self.__stamina = stamina
        self.__focus = focus
        self.__streak = 0
        self.__inventory = 0
        self.__status_effects = None
        self.REGEN_RATE_PER_ = 0.1
        self.MAX_STAMINA = 100
        self.MAX_FOCUS = 100

    def getName(self):
        return self.__name

    def getLevel(self):
        return self.__level

    def getTotalXp(self):
        return self.__total_xp

    def getStamina(self):
        return self.__stamina

    def getFocus(self):
        return self.__focus

    def getStreak(self):
        return self.__streak

    def getInventory(self):
        return self.__inventory.copy()

    def getStatusEffects(self):
        return self.__status_effects

    def setName(self, name: str):
        self.__name = name

    def setLevel(self, level: int):
        self.__level = level

    def setTotalXp(self, total_xp: int):
        self.__total_xp = total_xp

    def setStamina(self, stamina: int):
        self.__stamina = stamina

    def setFocus(self, focus: int):
        self.__focus = focus

    def setStreak(self, streak: int):
        self.__streak = streak

    def setInventory(self, inventory: int):
        self.__inventory = inventory

    def setStatusEffects(self, status_effects):
        self.__status_effects = status_effects

    #Will calculate the level based on skill tree progressions
    #and total xp earned from quests
    def calculateLevel(self,*args):
        ...

    
    