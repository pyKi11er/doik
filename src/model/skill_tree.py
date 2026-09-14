from __future__ import annotations
from dataclasses import dataclass, field
from typing import ClassVar
from model import Category
from math import exp

@dataclass
class SkillTree:
    XP_CURVE_BASE: ClassVar[int] = 100
    XP_CURVE_RATE: ClassVar[float] = 0.25
    BASE_LVL: ClassVar[int] = 1
    MAX_LVL: ClassVar[int] = 20
    
    tree_id: int | None = None
    ref_to_cat: Category | None = None
    child_nodes: list = field(default_factory=list)
    unlocked_nodes: list = field(default_factory=list)
    locked_nodes: list = field(default_factory=list)
    tree_name: str = ""
    tree_lvl: int = 1
    total_xp: float = 0


    @property
    def is_maxed(self):
        return self.tree_lvl >= self.MAX_LVL

    @property
    def xp_for_next(self):
        return self.calculateXPForNextLevel()


    #Calculates threshold xp for any level
    def calculateXPForLevel(self, lvl: int) -> float:
        if lvl <= self.BASE_LVL:
            return 0
        return self.XP_CURVE_BASE * exp(self.XP_CURVE_RATE * (lvl - 1))


    #Calculates the amount of overall xp a
    # character should have to reach the next level
    def calculateXPForNextLevel(self, lvl: int | None = None) -> float:
        if lvl is None:
            lvl = self.tree_lvl
        return self.calculateTreeLevel(lvl+1)

    # Needed to reset displayed xp after leveling up
    @property
    def xp_into_current_level(self) -> float:
        return self.total_xp - self.calculateXPForNextLevel(self.tree_lvl)

    # Needed to reset goal xp for a new level
    @property
    def xp_needed_for_current_level(self) -> float:
        if self.is_maxed:
            return 0
        return self.calculateXPForNextLevel() - self.calculateXPForLevel(self.tree_lvl)

    # Calculates which level should be judged by 
    # the amount of total_xp 
    def calculateTreeLevel(self) -> int:
        new_level = self.tree_lvl
        while (
            new_level < self.MAX_LVL and
            self.total_xp >= self.calculateXPForNextLevel(new_level)
        ):
            new_level += 1
        return new_level

            

    def addXP(self, reward_xp: float):
        self.total_xp += reward_xp
        self.tree_lvl = self.calculateTreeLevel()