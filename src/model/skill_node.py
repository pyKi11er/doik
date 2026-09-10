from dataclasses import dataclass

@dataclass
class SkillNode:
    def __init__(self):
        self.__node_id = None
        self.__skill_name = ""
        self.__parent_nodes = [] #array of SkillNode refs, a node can require multiple prior nodes
        self.__description = ""
        self.__embedding_vector = None
        self.__unlocking_xp = 0
        self.__category = None
        self.__state = 0 # state: 0 = locked, 1 = unlocked, 2 = mastered

    def getNodeId(self):
        return self.__node_id

    def getSkillName(self):
        return self.__skill_name

    def getParentNodes(self):
        return self.__parent_nodes.copy()

    def getDescription(self):
        return self.__description

    def getEmbeddingVector(self):
        return self.__embedding_vector

    def getUnlockingXp(self):
        return self.__unlocking_xp

    def getCategory(self):
        return self.__category

    def getState(self):
        return self.__state

    def setNodeId(self, node_id: int):
        self.__node_id = node_id

    def setSkillName(self, skill_name: str):
        self.__skill_name = skill_name

    def addParentNode(self, parent_node):
        self.__parent_nodes.append(parent_node)

    def setDescription(self, description: str):
        self.__description = description

    def setEmbeddingVector(self, embedding_vector: list):
        self.__embedding_vector = embedding_vector.copy() if embedding_vector else None

    def setUnlockingXp(self, unlocking_xp: int):
        self.__unlocking_xp = unlocking_xp

    def setCategory(self, category):
        self.__category = category

    def setState(self, state: int):
        self.__state = state