from dataclasses import dataclass, field
from typing import ClassVar
from src.model.skill_forest import SkillForest
from src.model.exceptions import CharacterError, CharacterSkillForestAlreadyExists
# The character class will hold the character's stats, inventory, and status effects.
@dataclass
class Character:
    REGEN_RATE_PER_HOUR: ClassVar[float] = 0.1
    MAX_STAMINA: ClassVar[int] = 100
    MAX_FOCUS: ClassVar[int] = 100

    character_id: int | None = None
    name: str = ""
    streak: int = 0
    inventory: int = 0
    status_effects: list = field(default_factory=list)
    attribute_stats: dict = field(default_factory=dict)
    

    _stamina: float = 100
    _focus: float = 100
    _ref_skill_forest: SkillForest | None = None

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

    @property
    def ref_skill_forest(self) -> SkillForest:
        return self._ref_skill_forest


    # Write-once: raises if a forest is already assigned, rather than silently
    # replacing it.
    @ref_skill_forest.setter
    def ref_skill_forest(self, skill_forest: SkillForest):
        if self._ref_skill_forest is not None:
            raise CharacterSkillForestAlreadyExists(
                f"Character {self.name!r} already has a SkillForest assigned."
            )
        self._ref_skill_forest = skill_forest
