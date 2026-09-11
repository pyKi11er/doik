from dataclasses import dataclass, field
from typing import ClassVar

# The character class will hold the character's stats, inventory, and status effects.
@dataclass
class Character:
    REGEN_RATE_PER_HOUR: ClassVar[float] = 0.1
    MAX_STAMINA: ClassVar[int] = 100
    MAX_FOCUS: ClassVar[int] = 100

    character_id: int | None = None
    name: str = ""
    level: int = 0  # was missing entirely - restored, since calculateLevel()
                     # needs somewhere to store its result
    total_xp: float = 0
    streak: int = 0
    inventory: int = 0
    status_effects: list = field(default_factory=list)
    attribute_stats: dict = field(default_factory=dict)

    _stamina: float = 100
    _focus: float = 100

    @property
    def stamina(self) -> float:
        return self._stamina

    @stamina.setter
    def stamina(self, val: float):
        self._stamina = max(0, min(val, self.MAX_STAMINA))

    @property
    def focus(self) -> float:
        return self._focus

    @focus.setter
    def focus(self, val: float):
        self._focus = max(0, min(val, self.MAX_FOCUS))

    # Will calculate the level based on skill tree progressions
    # and total xp earned from quests
    def calculateLevel(self, *args):
        ...