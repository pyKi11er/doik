from dataclasses import dataclass

class SkillTree:
    def __init__(self):
        self.__child_nodes = []
        self.__unlocked_nodes = []
        self.__locked_nodes = []
        self.__title = ""
        self.__tree_level = 0


    def getChildNodes(self):
        return self.__child_nodes.copy()

    def getUnlockedNodes(self):
        return self.__unlocked_nodes.copy()

    def getLockedNodes(self):
        return self.__locked_nodes.copy()

    def getTitle(self):
        return self.__title

    def getTreeLevel(self):
        return self.__tree_level

    def addChildNode(self, child_node):
        self.__child_nodes.append(child_node)

    def addUnlockedNode(self, unlocked_node):
        self.__unlocked_nodes.append(unlocked_node)

    def addLockedNode(self, locked_node):
        self.__locked_nodes.append(locked_node)

    def setTitle(self, title):
        self.__title = title

    def setTreeLevel(self, tree_level):
        self.__tree_level = tree_level

    def calculateTreeLevel(self):
        ...

    
    