from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from model import Category, Character, QuestMissingCategoryError, QuestCategoryZeroXP
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

    _reward_xp: int = field(init=False, repr=False)
    _completion_time: float = field(init=False, repr=False)
    _decay_rate: float = field(init=False, repr=False)
    _reward_tier: str = field(init=False, repr=False)
    _emotional_weight: float = field(init=False, repr=False)


    INTRINSIC_TIER_COSTS: ClassVar[dict] = {
        1: {"stamina": 5, "focus": 5},
        2: {"stamina": 10, "focus": 10},
        3: {"stamina": 17, "focus": 17},
        4: {"stamina": 25, "focus": 25},
        5: {"stamina": 36, "focus": 36}
    } # lookup table of tiers for our SLM

    MAX_XP_CATEGORY: ClassVar[int] = 100 #maximum xp a character can have in any skill tree
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
        self._reward_xp = self.calculateRewardXP()
        self._completion_time = self.calculateCompletionTime()
        self._decay_rate = self.calculateDecayRate()
        self._reward_tier = self.calculateRewardTier()
        self._emotional_weight = self.calculateEmotionalWeight()


    @property
    def reward_xp(self) -> int:
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

    def calculateDifficulty(self, character: Character) -> float:
        if self.category is  None:
            raise QuestMissingCategoryError(f"Quest {self.title!r} has no category set.")

        if self.category.xp_contribution <= 0:
            raise QuestCategoryZeroXP(
                f"Category {self.category.cat_name!r} has 0 XP contribution."
            )
        stamina_term = 5 * (self.stamina_cost / (character.stamina+1))
        focus_term = 7 * (self.focus_cost / (character.focus+1))
        return (self.MAX_XP_CATEGORY / self.category.xp_contribution) + stamina_term + focus_term
            

        

    def calculateRewardXP(self):
        ...

    def calculateCompletionTime(self):
        ...

    # Stamina cost and focus cost can either be manually set by the user or be
    # AI-approximated - kept as callable stubs rather than invoked automatically,
    # since the source of the value depends on origin.
    
        ...

    def calculateRewardTier(self):
        ...

    def calculateEmotionalWeight(self):
        ...

    def calculateDecayRate(self):
        ...