from dataclasses import dataclass

@dataclass
class SkillTree:
    def __init__(self):
        self.__tree_arr = []

    def getTreeArr(self):
        return self.__tree_arr.copy()
