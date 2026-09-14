from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from model import Category, Character, SkillTree, QuestMissingSkillTreeError, QuestInvalidSkillTreeLevelError
from typing import ClassVar


@dataclass
class Quest:

    tier: int | None = None #Tier will be determined by our future SLM, it will 
                            #give a tier based on the intrinsic tier costs
                            # from below then we have it as a field in our class and will be assigned by a different 
                            # class which will disassemble the json output from our SLM
    quest_id: int | None = None
    title: str = ""
    quest_type: int | None = None  # Main / Side / Daily. Origin (manual / brain-dump /
                                    # tavern) is not stored here - derivable by reverse
                                    # lookup from whichever log created this quest.
                                    
    stamina_cost: float = 0
    focus_cost: float = 0
    category: Category | None = None
    parent_quest: Quest | None = None
    state: int = 0
    time_of_creation: datetime = field(default_factory=datetime.now)
    time_of_completion: datetime | None = None
    recurring: bool = False

    _base_xp_reward: float = field(init=False, repr=False)
    _reward_xp: float = field(init=False, repr=False)
    _completion_time: float = field(init=False, repr=False)
    _decay_rate: float = field(init=False, repr=False)
    # _reward_tier: str = field(init=False, repr=False)
    _emotional_weight: float = field(init=False, repr=False)


    INTRINSIC_TIER_COSTS: ClassVar[dict] = {
        1: {"stamina": 5, "focus": 5, "base_xp_reward": 15},
        2: {"stamina": 10, "focus": 10, "base_xp_reward": 32.5},
        3: {"stamina": 17, "focus": 17, "base_xp_reward": 52.5},
        4: {"stamina": 25, "focus": 25, "base_xp_reward": 75},
        5: {"stamina": 36, "focus": 36, "base_xp_reward": 100}
    } # lookup table of tiers for our SLM

    MAX_XP_CATEGORY: ClassVar[int] = 100 # just a constant to ground the difficulty
    STAMINA_WEIGHT: ClassVar[int] = 5 # stamina factor
    FOCUS_WEIGHT: ClassVar[int] = 7 # focus factor which is greater as logically focus is more important

    def __post_init__(self):
        if self.tier is not None and self.tier not in self.INTRINSIC_TIER_COSTS:
            raise ValueError(
                f"Unknown quest tier: {self.tier!r}. "
                f"Expected one of {sorted(self.INTRINSIC_TIER_COSTS)}."
            )

        if self.tier is not None:
            self.stamina_cost = self.calculateStaminaCost()
            self.focus_cost = self.calculateFocusCost()
        self._reward_xp = self.calculateRewardXP() # with our multiplier
        self._base_reward_xp = self.calculateBaseRewardXP() #getting it from lookup table
        self._completion_time = self.calculateCompletionTime()
        self._decay_rate = self.calculateDecayRate()

        # self._reward_tier = self.calculateRewardTier()
        
        self._emotional_weight = self.calculateEmotionalWeight()


    @property
    def base_reward_xp(self) -> float:
        return self._base_reward_xp

    @property
    def reward_xp(self) -> float:
        return self._reward_xp

    @property
    def completion_time(self) -> float:
        return self._completion_time

    @property
    def decay_rate(self) -> float:
        return self._decay_rate

    @property
    def reward_tier(self) -> str:
        return self._reward_tier

    @property
    def emotional_weight(self) -> float:
        return self._emotional_weight


    def calculateStaminaCost(self) -> int:
        return self.INTRINSIC_TIER_COSTS[self.tier]["stamina"]

    def calculateFocusCost(self) -> int:
        return self.INTRINSICE_TIER_COST[self.tier]["focus"]

    def calculateBaseRewardXP(self) -> float:
        return self.INTRINSIC_TIER_COSTS[self.tier]["base_xp_reward"]

    def calculateDifficulty(self, character: Character, skill_tree: SkillTree) -> float:
        if skill_tree is None:
            raise QuestMissingSkillTreeError(
                f"Quest {self.title!r} was not given a SkillTree to calculate difficulty against."
            )


        if skill_tree.tree_lvl <= 0:
            raise QuestInvalidSkillTreeLevelError(
                f"SkillTree {skill_tree.tree_name!r} has a non-positive tree_lvl "
                f"({skill_tree.tree_lvl}); difficulty is undefined."
            )
        stamina_term = 5 * (self.stamina_cost / (character.stamina+1))
        focus_term = 7 * (self.focus_cost / (character.focus+1))
        return (self.MAX_XP_CATEGORY / skill_tree.tree_lvl) + stamina_term + focus_term
            

        

    def calculateRewardXP(self):
        multiplier = 1 + (self.calculateDifficulty() / 100)
        return self.base_reward_xp * multiplier

    def calculateCompletionTime(self):
        ...
    
        ...

    # def calculateRewardTier(self):
    #     ...

    def calculateEmotionalWeight(self):
        ...

    def calculateDecayRate(self):
        ...