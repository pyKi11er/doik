from __future__ import annotations
from dataclasses import dataclass, field
from model import Log

@dataclass
class Questline:
    questline_id: int | None = None
    questline_name: str = ""
    questline_desc: str = ""
    questline_xp_contribution: float = 0
    child_quests: list = field(default_factory=list)
    booster_for_streak: int = 0
    ref_to_log: Log | None = None
    questline_color: str = ""
    parent_questline: Questline | None = None
    # No reference back to the originating BrainDump - BrainDump already stores a
    # forward ref_to_questline; a back-reference here would be redundant and risks
    # the two going out of sync.

    def addChildQuest(self, child_quest):
        self.child_quests.append(child_quest)

    # Will determine the xp_contribution later on by receiving it from logs
    def incrementXpContribution(self, xp_contribution: int):
        self.questline_xp_contribution += xp_contribution