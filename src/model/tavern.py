from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Tavern:
    tavern_offer_id: int | None = None
    timestamp: datetime = field(default_factory=datetime.now)
    pool_of_choices: list = field(default_factory=list)
    context_state: str = ""  # time of day, remaining stamina, remaining focus,
                              # recent completions
    final_choices: list = field(default_factory=list)
    explanation: str = ""
    reward: str = ""  # flavor/response text on accept, e.g. "The keeper nods
                       # approvingly" - NOT numeric, actual XP/gold lives on Quest
    mood: int | None = None

    def setPoolOfChoices(self, pool_of_choices):
        self.pool_of_choices.extend(pool_of_choices)

    def setFinalChoices(self, final_choices):
        self.final_choices.extend(final_choices)