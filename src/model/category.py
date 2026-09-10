class Category:
    def __init__(self):
        self.__category_name = ""
        self.__category_description = ""
        self.__xp_contribution = 0
        self.__color = None
        self.__parent_category = None #One of the core 5 categories
        self.__category_id = None

    def getCategoryName(self):
        return self.__category_name

    def getCategoryDescription(self):
        return self.__category_description

    def getCategoryId(self):
        return self.__category_id

    def getXpContribution(self):
        return self.__xp_contribution

    def getColor(self):
        return self.__color

    def getParentCategory(self):
        return self.__parent_category

    def setCategoryName(self, category_name: str):
        self.__category_name = category_name

    def setCategoryDescription(self, category_description: str):    
        self.__category_description = category_description

    def setCategoryId(self, category_id: int):
        self.__category_id = category_id

    def setCategoryColor(self, color):
        self.__color = color

    def setParentCategory(self, parent_category):
        self.__parent_category = parent_category

    #Will determine the xp_contribution later on by receiving it from logs
    def incrementXpContribution(self, xp_contribution: int):
        self.__xp_contribution += xp_contribution

    #Will determine category based on category_id if category_id between
    #0-5 then parent_category is null if category_id is above that
    #will use an algorithm to determine the parent category and assign the id
    # of the parent
    def determineCategory(self):
        ...
