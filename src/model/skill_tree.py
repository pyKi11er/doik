from dataclasses import dataclass

import model.category as Category

class SkillTree:
    def __init__(self):
        self._tree_id = None
        self.__ref_to_category = None
        self.__child_nodes = []
        self.__unlocked_nodes = []
        self.__locked_nodes = []
        self.__tree_title = ""
        self.__tree_level = 0

    def getTreeId(self):
        return self._tree_id

    def getRefToCategory(self):
        return self.__ref_to_category

    def getChildNodes(self):
        return self.__child_nodes.copy()

    def getUnlockedNodes(self):
        return self.__unlocked_nodes.copy()

    def getLockedNodes(self):
        return self.__locked_nodes.copy()

    def getTreeTitle(self):
        return self.__tree_title

    def getTreeLevel(self):
        return self.__tree_level

    def addChildNode(self, child_node):
        self.__child_nodes.append(child_node)

    def addUnlockedNode(self, unlocked_node):
        self.__unlocked_nodes.append(unlocked_node)

    def addLockedNode(self, locked_node):
        self.__locked_nodes.append(locked_node)

    def setTreeTitle(self, tree_title):
        self.__tree_title = tree_title

    def setTreeLevel(self, tree_level):
        self.__tree_level = tree_level

    def setTreeId(self, tree_id: int):
        self._tree_id = tree_id

    def setRefCategory(self, category: Category):
        self.__ref_to_category = category

    def calculateTreeLevel(self):
        ...

    
    