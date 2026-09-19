from model import Quest, Character, SkillTree
from model.exceptions import QuestError,  QuestMissingCategoryError, QuestMissingSkillTreeError, QuestInvalidSkillTreeLevelError

class QuestCalculator:

    INTRINSIC_TIER_COSTS = {
            1: {"stamina": 5, "focus": 5, "base_xp_reward": 15},
            2: {"stamina": 10, "focus": 10, "base_xp_reward": 32.5},
            3: {"stamina": 17, "focus": 17, "base_xp_reward": 52.5},
            4: {"stamina": 25, "focus": 25, "base_xp_reward": 75},
            5: {"stamina": 36, "focus": 36, "base_xp_reward": 100}
        } # lookup table of tiers for our SLM

    MAX_XP_CATEGORY = 100 # just a constant to ground the difficulty
    STAMINA_WEIGHT = 5 # stamina factor
    FOCUS_WEIGHT = 7 # focus factor which is greater as logically focus is more important


    @staticmethod
    def calculateStaminaCost(quest: Quest) -> int:
        return QuestCalculator.INTRINSIC_TIER_COSTS[quest.tier]["stamina"]


    @staticmethod
    def calculateFocusCost(quest: Quest) -> int:
        return QuestCalculator.INTRINSICE_TIER_COST[quest.tier]["focus"]


    @staticmethod
    def calculateBaseRewardXP(quest: Quest) -> float:
        return QuestCalculator.INTRINSIC_TIER_COSTS[quest.tier]["base_xp_reward"]



    
    @staticmethod
    def calculateDifficulty(quest: Quest, character: Character, skill_tree: SkillTree) -> float:
        if skill_tree is None:
            raise QuestMissingSkillTreeError(
                f"Quest {quest.title!r} was not given a SkillTree to calculate difficulty against."
            )


        if skill_tree.tree_lvl <= 0:
            raise QuestInvalidSkillTreeLevelError(
                f"SkillTree {skill_tree.tree_name!r} has a non-positive tree_lvl "
                f"({skill_tree.tree_lvl}); difficulty is undefined."
            )
        stamina_term = 5 * (QuestCalculator.calculateStaminaCost(quest) / (character.stamina+1))
        focus_term = 7 * (QuestCalculator.calculateFocusCost(quest) / (character.focus+1))
        return (QuestCalculator.MAX_XP_CATEGORY / skill_tree.tree_lvl) + stamina_term + focus_term
            

        


    @staticmethod
    def calculateRewardXP(quest: Quest, character: Character, skill_tree: SkillTree) -> float:
        multiplier = 1 + (QuestCalculator.calculateDifficulty(quest, character, skill_tree) / 100)
        return QuestCalculator.calculateBaseRewardXP(quest) * multiplier



    @staticmethod
    def calculateCompletionTime(self):
        ...


    # def calculateRewardTier(self):
    #     ...

    @staticmethod
    def calculateEmotionalWeight(self):
        ...


    @staticmethod
    def calculateDecayRate(self):
        ...