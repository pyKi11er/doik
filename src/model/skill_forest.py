# Renamed from SkillTree to SkillForest to resolve the name collision with the
# per-category tree class in parent_tree.py (that one is now the "SkillTree").
# Worth deciding if this needs to stay a real class at all - it currently holds
# no state beyond a plain list of trees, so it could just as easily be an
# implicit query/collection at the app level rather than a persisted entity.
class SkillForest:
    def __init__(self):
        self.__tree_arr = []

    def getTreeArr(self):
        return self.__tree_arr.copy()

    def addTree(self, tree):
        self.__tree_arr.append(tree)