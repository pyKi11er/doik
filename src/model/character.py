from dataclasses import dataclass


#The character class will hold the character's stats, inventory, and status effects.
@dataclass
class Character:
    REGEN_RATE_PER_ = 0.1
    MAX_STAMINA = 100
    MAX_FOCUS = 100

    def __init__(self, stamina :int, focus : int):
        self.__character_id = None
        self.__name = ""
        self.__total_xp = 0
        self.__stamina = stamina
        self.__focus = focus
        self.__streak = 0
        self.__inventory = 0
        self.__status_effects = []
        self.__attribute_stats = {}
        self.__level = self.calculateLevel()
        #level depends on total_xp / attribute_stats, both set above,
        # so it must be calculated after they exist.

    def getCharacterId(self):
        return self.__character_id

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
        return self.__inventory

    def getStatusEffects(self):
        return self.__status_effects.copy()

    def getAttributeStats(self):
        return self.__attribute_stats.copy()

    def setCharacterId(self, character_id: int):
        self.__character_id = character_id

    def setName(self, name: str):
        self.__name = name

    def setLevel(self, level: int):
        self.__level = level

    def setTotalXp(self, total_xp: int):
        self.__total_xp = total_xp

    def setStamina(self, stamina: int):
        self.__stamina = max(0,min(stamina,self.MAX_STAMINA))

    def setFocus(self, focus: int):
        self.__focus = max(0,min(focus,self.MAX_FOCUS))

    def setStreak(self, streak: int):
        self.__streak = streak

    def setInventory(self, inventory: int):
        self.__inventory = inventory

    def setStatusEffects(self, status_effects: list):
        self.__status_effects = status_effects.copy()

    def setAttributeStats(self, attribute_stats: dict):
        self.__attribute_stats = attribute_stats.copy()
    #Will calculate the level based on skill tree progressions
    #and total xp earned from quests
    def calculateLevel(self,*args):
        ...

    
    