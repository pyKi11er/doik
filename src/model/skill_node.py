from dataclasses import dataclass

@dataclass
class SkillNode:
    def __init__(self):
        self.__skill_name = ""
        self.__skill_level = 0
        self.__children = []
        self.__description = ""
        self.__embedding_vector = None
        self.__unlocking_xp = 0
        self.__category = None
        self.__state = 0

    def getSkillName(self):
        return self.__skill_name

    def getSkillLevel(self):
        return self.__skill_level

    def getChildren(self):
        return self.__children.copy()

    def addChild(self, child_node):
        self.__children.append(child_node)

    def getDescription(self):
        return self.__description

    def getEmbeddingVector(self):
        return self.__embedding_vector

    def getUnlockingXp(self):
        return self.__unlocking_xp

    def getCategory(self):
        return self.__category