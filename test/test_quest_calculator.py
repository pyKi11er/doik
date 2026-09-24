import pytest
from src.model.quest import Quest
from src.model.category import Category
from src.model.skill_tree import SkillTree
from src.model.character import Character
from src.calculators.quest_calculator import QuestCalculator
from src.model.exceptions import QuestMissingCategoryError, QuestInvalidSkillTreeLevelError, QuestMissingSkillTreeError, QuestMissingCharacterError, QuestIsNone


@pytest.fixture
def category():
    return Category(cat_name="Discipline")

@pytest.fixture
def skill_tree(category):
    return SkillTree(ref_to_cat = category, tree_name="Discipline" , tree_lvl = 5)

@pytest.fixture
def character():
    return Character(name = "Hero", _stamina = 50, _focus = 50)


@pytest.fixture
def quest_default_tier3(category):
    return Quest(title = "20 pushups", tier = 3, category = category)



class TestTierLookups:
    @pytest.mark.parametrize("tier", [1, 2, 3, 4, 5])
    def test_stamina_cost_matches_table(self, category, tier):
        quest = Quest(title="X", tier=tier, category=category)
        assert QuestCalculator.calculateStaminaCost(quest) == QuestCalculator.INTRINSIC_TIER_COSTS[tier]["stamina"]
 
    @pytest.mark.parametrize("tier", [1, 2, 3, 4, 5])
    def test_focus_cost_matches_table(self, category, tier):
        quest = Quest(title="X", tier=tier, category=category)
        assert QuestCalculator.calculateFocusCost(quest) == QuestCalculator.INTRINSIC_TIER_COSTS[tier]["focus"]
 
    @pytest.mark.parametrize("tier", [1, 2, 3, 4, 5])
    def test_base_reward_xp_matches_table(self, category, tier):
        quest = Quest(title="X", tier=tier, category=category)
        assert QuestCalculator.calculateBaseRewardXP(quest) == QuestCalculator.INTRINSIC_TIER_COSTS[tier]["base_xp_reward"]
 
    def test_higher_tier_costs_more(self, category):
        quests = [Quest(title="X", tier=t, category=category) for t in range(1, 6)]
        stamina_costs = [QuestCalculator.calculateStaminaCost(q) for q in quests]
        assert stamina_costs == sorted(stamina_costs)
 



class TestCalculateDifficulty:
    def test_raises_when_no_quest(self, character, skill_tree):
        with pytest.raises(QuestIsNone):
            QuestCalculator.calculateDifficulty(None, character, skill_tree)
    def test_raises_when_no_character(self, quest_default_tier3, skill_tree):
        with pytest.raises(QuestMissingCharacterError):
            QuestCalculator.calculateDifficulty(quest_default_tier3, None, skill_tree)

    def test_raises_when_no_skill_tree(self, quest_default_tier3, character):
        with pytest.raises(QuestMissingSkillTreeError):
            QuestCalculator.calculateDifficulty(quest_default_tier3, character, None)

    def test_raises_when_negative_skilltree_level(self, quest_default_tier3, character, category):
        broken_tree = SkillTree(tree_name = 'Broken', ref_to_cat = category, tree_lvl = -1)  
        with pytest.raises(QuestInvalidSkillTreeLevelError):
            QuestCalculator.calculateDifficulty(quest_default_tier3, character, broken_tree)


    def test_lower_stamina_makes_it_harder(self, quest_default_tier3, skill_tree):
        tired = Character(name="Tired", _stamina = 10, _focus = 99)
        rested = Character(name="Rested", _stamina = 99, _focus = 99)
        tired_difficulty = QuestCalculator.calculateDifficulty(quest_default_tier3, tired, skill_tree)
        rested_difficulty = QuestCalculator.calculateDifficulty(quest_default_tier3, rested, skill_tree)

        assert tired_difficulty > rested_difficulty


    def test_lower_focus_makes_it_harder(self, quest_default_tier3, skill_tree):
        tired = Character(name="Tired", _stamina = 99, _focus = 10)
        rested = Character(name = "Rested", _stamina = 99, _focus = 99)
        tired_difficulty = QuestCalculator.calculateDifficulty(quest_default_tier3, tired, skill_tree)
        rested_difficulty = QuestCalculator.calculateDifficulty(quest_default_tier3, rested, skill_tree)

        assert tired_difficulty > rested_difficulty


    def test_lower_skilltree_level_makes_harder(self, quest_default_tier3, character, category):
        low_skill_tree = SkillTree(ref_to_cat = category, tree_name = "Low Discipline")
        high_skill_tree = SkillTree(ref_to_cat = category, tree_name = "High Discipline", tree_lvl = 20)
        low_skill_diff = QuestCalculator.calculateDifficulty(quest_default_tier3, character, low_skill_tree)
        high_skill_diff = QuestCalculator.calculateDifficulty(quest_default_tier3, character, high_skill_tree)

        assert low_skill_diff > high_skill_diff

    def test_matches_formula(self, quest_default_tier3, character, skill_tree):
        expected = (
            (100/skill_tree.tree_lvl) + (5 * (QuestCalculator.calculateStaminaCost(quest_default_tier3) / (character.stamina + 1)))
            + (7 * (QuestCalculator.calculateFocusCost(quest_default_tier3) / (character.focus + 1)))
        )
        real_result = QuestCalculator.calculateDifficulty(quest_default_tier3, character, skill_tree)
        assert real_result == pytest.approx(expected)


class TestCalculateReward:

    def test_matches_formula_reward(self, quest_default_tier3, character, skill_tree):
        difficulty = QuestCalculator.calculateDifficulty(quest_default_tier3, character, skill_tree)
        expected = QuestCalculator.calculateBaseRewardXP(quest_default_tier3) * (1 + (difficulty / 100))
        real_result = QuestCalculator.calculateRewardXP(quest_default_tier3, character, skill_tree)

        assert real_result == pytest.approx(expected)


    def test_harder_earns_more(self, quest_default_tier3, skill_tree):
        tired = Character(name="Tired", _stamina = 99, _focus = 10)
        rested = Character(name = "Rested", _stamina = 99, _focus = 99)

        result_tired = QuestCalculator.calculateRewardXP(quest_default_tier3, tired, skill_tree)
        result_rested = QuestCalculator.calculateRewardXP(quest_default_tier3, rested, skill_tree)

        assert result_tired > result_rested

    def test_propagates_missing_skilltree(self, quest_default_tier3, character):
        with pytest.raises(QuestMissingSkillTreeError):
            QuestCalculator.calculateRewardXP(quest_default_tier3, character, None)

    def test_propagates_missing_character(self, quest_default_tier3, skill_tree):
        with pytest.raises(QuestMissingCharacterError):
            QuestCalculator.calculateRewardXP(quest_default_tier3, None, skill_tree)

    def test_propagates_missing_character(self, character, skill_tree):
        with pytest.raises(QuestIsNone):
            QuestCalculator.calculateRewardXP(None, character, skill_tree)
    

    