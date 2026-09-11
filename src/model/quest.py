from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from model import Category

@dataclass
class Quest:
    quest_id: int | None = None
    title: str = ""
    quest_type: int | None = None  # Main / Side / Daily. Origin (manual / brain-dump /
                                    # tavern) is NOT stored here - derivable by reverse
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

    # Difficulty is intentionally NOT a stored field as the design it's
    # computed at display time as f(stamina_cost, focus_cost, character.stamina,
    # character.focus), not a fixed intrinsic value.

    def __post_init__(self):
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

    def calculateRewardXP(self):
        ...

    def calculateCompletionTime(self):
        ...

    # Stamina cost and focus cost can either be manually set by the user or be
    # AI-approximated - kept as callable stubs rather than invoked automatically,
    # since the source of the value depends on origin.
    def calculateStaminaCost(self):
        ...

    def calculateFocusCost(self):
        ...

    def calculateRewardTier(self):
        ...

    def calculateEmotionalWeight(self):
        ...

    def calculateDecayRate(self):
        ...