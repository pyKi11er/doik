import pytest
from src.model.character import Character
from src.model.skill_forest import SkillForest
from src.model.skill_tree import SkillTree
from src.model.category import Category
from src.model.exceptions import CharacterMissingSkillForestError
from src.calculators.character_calculator import CharacterCalculator


@pytest.fixture
def character_no_forest():
    return Character(name="Hero")


@pytest.fixture
def character_empty_forest():
    char = Character(name="Hero")
    char.ref_skill_forest = SkillForest()
    return char


@pytest.fixture
def character_with_trees():
    char = Character(name="Hero")
    forest = SkillForest()
    # (name, tree_lvl, total_xp)
    for name, lvl, xp in [
        ("Discipline", 4, 300),
        ("Body", 2, 90),
        ("Creativity", 6, 800),
        ("Social", 1, 0),
        ("Focus", 3, 150),
    ]:
        cat = Category(cat_name=name)
        forest.addTree(SkillTree(tree_name=name, ref_to_cat=cat, tree_lvl=lvl, total_xp=xp))
    char.ref_skill_forest = forest
    return char


class TestCalculateLevel:
    def test_raises_when_no_forest(self, character_no_forest):
        with pytest.raises(CharacterMissingSkillForestError):
            CharacterCalculator.calculateLevel(character_no_forest)

    def test_zero_for_empty_forest(self, character_empty_forest):
        assert CharacterCalculator.calculateLevel(character_empty_forest) == 0

    def test_sums_tree_levels(self, character_with_trees):
        # 4 + 2 + 6 + 1 + 3
        assert CharacterCalculator.calculateLevel(character_with_trees) == 16


class TestGetTotalXP:
    def test_raises_when_no_forest(self, character_no_forest):
        with pytest.raises(CharacterMissingSkillForestError):
            CharacterCalculator.getTotalXP(character_no_forest)

    def test_zero_for_empty_forest(self, character_empty_forest):
        assert CharacterCalculator.getTotalXP(character_empty_forest) == 0

    def test_sums_tree_xp(self, character_with_trees):
        # 300 + 90 + 800 + 0 + 150
        assert CharacterCalculator.getTotalXP(character_with_trees) == 1340