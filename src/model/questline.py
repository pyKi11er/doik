class Questline:
    def __init__(self):
        self.__questline_id = None
        self.__questline_name = ""
        self.__questline_description = ""
        self.__questline_xp_contribution = 0
        self.__child_quests = []
        self.__booster_for_streak = 0
        self.__ref_to_log = None
        self.__questline_color = None
        self.__parent_questline = None
        # No reference back to the originating BrainDump. BrainDump already
        # stores a forward ref_to_questline, a back-reference here would be
        # redundant and risks the two going out of sync.

    def getQuestlineId(self):
        return self.__questline_id

    def getQuestlineName(self):
        return self.__questline_name

    def getQuestlineDescription(self):
        return self.__questline_description

    def getQuestlineXpContribution(self):
        return self.__questline_xp_contribution

    def getChildQuests(self):
        return self.__child_quests.copy()

    def getBoosterForStreak(self):
        return self.__booster_for_streak

    def getRefToLog(self):
        return self.__ref_to_log

    def getQuestlineColor(self):
        return self.__questline_color

    def getParentQuestline(self):
        return self.__parent_questline

    def setQuestlineId(self, questline_id: int):
        self.__questline_id = questline_id

    def setQuestlineName(self, questline_name: str):
        self.__questline_name = questline_name

    def setQuestlineDescription(self, questline_description: str):
        self.__questline_description = questline_description

    def setBoosterForStreak(self, booster_for_streak: int):
        self.__booster_for_streak = booster_for_streak

    def setRefToLog(self, ref_to_log):
        self.__ref_to_log = ref_to_log

    def setQuestlineColor(self, questline_color):
        self.__questline_color = questline_color

    def setParentQuestline(self, parent_questline):
        self.__parent_questline = parent_questline

    def addChildQuest(self, child_quest):
        self.__child_quests.append(child_quest)

    # Will determine the xp_contribution later on by receiving it from logs
    def incrementXpContribution(self, xp_contribution: int):
        self.__questline_xp_contribution += xp_contribution