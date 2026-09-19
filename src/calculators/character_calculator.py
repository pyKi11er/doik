from model import Character
from model.exceptions import CharacterMissingSkillForestError
class CharacterCalculator:

    @staticmethod
    def calculateLevel(char: Character) -> int:
        if char.ref_skill_forest is None:
            raise CharacterMissingSkillForestError(
                f"Character {char.name!r} has no Skill Forest set"
            )
        return sum(tree.tree_lvl for tree in char.ref_skill_forest.tree_arr)

    @staticmethod
    def getTotalXP(char: Character) -> float:
        if char.ref_skill_forest is None:
            raise CharacterMissingSkillForestError(
                f"Character {char.name!r} has no Skill Forest set"
            )
        return sum(tree.total_xp for tree in char.ref_skill_forest.tree_arr)