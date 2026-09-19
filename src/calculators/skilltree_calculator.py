from model import SkillTree
from math import exp, sin, pi

class SkillTreeCalculator:
    XP_CURVE_BASE = 100
    XP_CURVE_RATE = 0.25
    BASE_LVL = 1
    MAX_LVL = 20
    FRICTION_AMPLITUDE = -0.4
    FRICTION_WIDTH = 7


    @staticmethod
    def is_maxed(skill_tree: SkillTree) -> bool:
        return skill_tree.tree_lvl >= SkillTreeCalculator.MAX_LVL

    # Friction for implementation of a real learning curve where around levels 5-8 
    # the gaining xp becomes significantly harder then gradually after reaching level 15 
    # our regular exponential grind begins
    @staticmethod
    def calculateFrictionCoef(lvl: int) -> float:
        if lvl >= 15:
            return 1
        return 1 + (SkillTreeCalculator.FRICTION_AMPLITUDE * sin((pi * lvl) / SkillTreeCalculator.FRICTION_WIDTH)) #1 - 0.4 * sin(lvl * pi/7)


    #Calculates threshold xp for any level
    @staticmethod
    def calculateXPForLevel(lvl: int) -> float:
        if lvl <= SkillTreeCalculator.BASE_LVL:
            return 0
        friction = SkillTreeCalculator.calculateFrictionCoef(lvl)
        return (SkillTreeCalculator.XP_CURVE_BASE * exp(SkillTreeCalculator.XP_CURVE_RATE * (lvl - 1))) * friction # 100 * e^(0.25*lvl) * friction



    #Calculates the amount of overall xp a
    # character should have to reach the next level
    # Needed to reset displayed xp after leveling up
    @staticmethod
    def calculateXPForNextLevel(lvl: int) -> float:
        return SkillTreeCalculator.calculateXPForLevel(lvl+1)


    # Needed For outsiders to not mangle with lvl of the tree and instead just pass the tree
    @staticmethod
    def calculateXPForNext(skill_tree: SkillTree) -> float:
        return SkillTreeCalculator.calculateXPForNextLevel(skill_tree.tree_lvl)
    

    # Needed to reset current xp in the level for UI (gained more then the goal was so gained xp - old lvl goal)
    @staticmethod
    def calculateXPIntoCurrentLevel(skill_tree: SkillTree) -> float:
        return skill_tree.total_xp - SkillTreeCalculator.calculateXPForLevel(skill_tree.tree_lvl)

    
    # Needed to reset goal xp for a new level (so the new goal will become new level - old level)
    @staticmethod
    def calculateXPNeededForCurrentLevel(skill_tree: SkillTree) -> float:
        if SkillTreeCalculator.isMaxed(skill_tree):
            return 0
        return (
            SkillTreeCalculator.calculateXPForNext(skill_tree)
            - SkillTreeCalculator.calculateXPForLevel(skill_tree.tree_lvl)
        )


    # Calculates which level should be judged by 
    # the amount of total_xp 
    def calculateTreeLevel(skill_tree: SkillTree) -> int:
        new_level = skill_tree.tree_lvl
        while (
            new_level < SkillTreeCalculator.MAX_LVL and
            skill_tree.total_xp >= SkillTreeCalculator.calculateXPForNextLevel(new_level)
        ):
            new_level += 1
        return new_level
