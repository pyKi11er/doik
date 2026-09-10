from dataclasses import dataclass
from time import datetime

#A class for future implementation a lanuage model
# for determining the user's current sitation and generate
# quests for him.
@dataclass
class BrainDump:
    def __init__(self):
        self.__brain_dump_id = None
        self.__text = ""
        self.__timestamp = datetime.now()
        self.__embedding_vector = []
        self.__ref_to_questline = None

    def getBrainDumpId(self):
        return self.__brain_dump_id

    def getText(self):
        return self.__text

    def getTimestamp(self):
        return self.__timestamp

    def getEmbeddingVector(self):
        return self.__embedding_vector.copy()

    def getRefToQuestline(self):
        return self.__ref_to_questline

    def setBrainDumpId(self, brain_dump_id: int):
        self.__brain_dump_id = brain_dump_id

    def setText(self, text: str):
        self.__text = text

    def setEmbeddingVector(self, embedding_vector: list):
        self.__embedding_vector = embedding_vector.copy()

    def setRefToQuestline(self, ref_to_questline):
        self.__ref_to_questline = ref_to_questline