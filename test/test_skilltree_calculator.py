import pytest
from math import exp, sin, pi
from src.model.skill_tree import SkillTree
from src.model.category import Category
from src.calculators.skilltree_calculator import SkillTreeCalculator


@pytest.fixture
def category():
    return Category(cat_name="Discipline")


@pytest.fixture
def tree_base(category):
    return SkillTree(tree_name="Discipline", ref_to_cat=category)  # tree_lvl=1, total_xp=0


@pytest.fixture
def tree_mid(category):
    return SkillTree(tree_name="Discipline", ref_to_cat=category, tree_lvl=10, total_xp=1800)


@pytest.fixture
def tree_maxed(category):
    return SkillTree(tree_name="Discipline", ref_to_cat=category, tree_lvl=20, total_xp=1_000_000)


class TestIsMaxed:
    def test_false_below_max(self, tree_base):
        assert SkillTreeCalculator.isMaxed(tree_base) is False

    def test_true_at_max(self, tree_maxed):
        assert SkillTreeCalculator.isMaxed(tree_maxed) is True

    def test_true_above_max_lvl_value(self, category):
        tree = SkillTree(tree_name="X", ref_to_cat=category, tree_lvl=25)
        assert SkillTreeCalculator.isMaxed(tree) is True


class TestCalculateFrictionCoef:
    def test_returns_one_at_and_above_15(self):
        for lvl in (15, 16, 20, 50):
            assert SkillTreeCalculator.calculateFrictionCoef(lvl) == 1

    @pytest.mark.parametrize("lvl,expected", [
        (1, 0.826),
        (2, 0.687),
        (3, 0.610),
        (7, 1.000),
        (9, 1.313),
        (10, 1.390),
        (14, 1.000),
    ])
    def test_known_values(self, lvl, expected):
        assert SkillTreeCalculator.calculateFrictionCoef(lvl) == pytest.approx(expected, abs=1e-3)

    def test_matches_raw_formula(self):
        lvl = 6
        expected = 1 + (-0.4 * sin((pi * lvl) / 7))
        assert SkillTreeCalculator.calculateFrictionCoef(lvl) == pytest.approx(expected)


class TestCalculateXPForLevel:
    def test_zero_at_or_below_base_level(self):
        assert SkillTreeCalculator.calculateXPForLevel(1) == 0
        assert SkillTreeCalculator.calculateXPForLevel(0) == 0
        assert SkillTreeCalculator.calculateXPForLevel(-5) == 0

    def test_positive_above_base_level(self):
        assert SkillTreeCalculator.calculateXPForLevel(2) > 0

    def test_matches_formula_with_friction(self):
        lvl = 9
        friction = SkillTreeCalculator.calculateFrictionCoef(lvl)
        expected = 100 * exp(0.25 * (lvl - 1)) * friction
        assert SkillTreeCalculator.calculateXPForLevel(lvl) == pytest.approx(expected)


class TestCalculateXPForNextLevel:
    def test_next_level_equals_threshold_for_lvl_plus_one(self):
        for lvl in range(1, 19):
            assert SkillTreeCalculator.calculateXPForNextLevel(lvl) == pytest.approx(
                SkillTreeCalculator.calculateXPForLevel(lvl + 1)
            )


class TestCalculateXPForNext:
    def test_uses_trees_current_level(self, tree_mid):
        assert SkillTreeCalculator.calculateXPForNext(tree_mid) == pytest.approx(
            SkillTreeCalculator.calculateXPForNextLevel(tree_mid.tree_lvl)
        )


class TestXPIntoAndNeededForCurrentLevel:
    def test_into_current_level_at_fresh_tree(self, tree_base):
        assert SkillTreeCalculator.calculateXPIntoCurrentLevel(tree_base) == 0

    def test_into_current_level_matches_subtraction(self, tree_mid):
        expected = tree_mid.total_xp - SkillTreeCalculator.calculateXPForLevel(tree_mid.tree_lvl)
        assert SkillTreeCalculator.calculateXPIntoCurrentLevel(tree_mid) == pytest.approx(expected)

    def test_needed_is_zero_when_maxed(self, tree_maxed):
        assert SkillTreeCalculator.calculateXPNeededForCurrentLevel(tree_maxed) == 0

    def test_needed_matches_bar_width(self, tree_mid):
        expected = (
            SkillTreeCalculator.calculateXPForNext(tree_mid)
            - SkillTreeCalculator.calculateXPForLevel(tree_mid.tree_lvl)
        )
        assert SkillTreeCalculator.calculateXPNeededForCurrentLevel(tree_mid) == pytest.approx(expected)


class TestCalculateTreeLevel:
    def test_stays_same_level_when_xp_insufficient(self, category):
        tree = SkillTree(tree_name="X", ref_to_cat=category, tree_lvl=1, total_xp=10)
        assert SkillTreeCalculator.calculateTreeLevel(tree) == 1

    def test_levels_up_by_one_when_threshold_crossed(self, category):
        threshold = SkillTreeCalculator.calculateXPForNextLevel(10)
        tree = SkillTree(tree_name="X", ref_to_cat=category, tree_lvl=10, total_xp=threshold)
        assert SkillTreeCalculator.calculateTreeLevel(tree) == 11

    def test_jumps_multiple_levels_on_huge_xp(self, category):
        tree = SkillTree(tree_name="X", ref_to_cat=category, tree_lvl=1, total_xp=5000)
        assert SkillTreeCalculator.calculateTreeLevel(tree) == 16

    def test_caps_at_max_level(self, category):
        tree = SkillTree(tree_name="X", ref_to_cat=category, tree_lvl=1, total_xp=10_000_000)
        assert SkillTreeCalculator.calculateTreeLevel(tree) == SkillTreeCalculator.MAX_LVL

    def test_does_not_mutate_the_tree(self, category):
        tree = SkillTree(tree_name="X", ref_to_cat=category, tree_lvl=1, total_xp=5000)
        SkillTreeCalculator.calculateTreeLevel(tree)
        assert tree.tree_lvl == 1