from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from model import Category


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
                                    
    category: Category | None = None
    parent_quest: Quest | None = None
    state: int = 0
    time_of_creation: datetime = field(default_factory=datetime.now)
    time_of_completion: datetime | None = None
    recurring: bool = False
    character_id: int | None = None # owner of the quest



    # THESE SHOULD BE CHANGED FROM CACHED ATTRIBUTES TO READ ONLY FUNCTION CALLS 
    # WHICH WILL BE IMPLEMENTED IN QuestCalculator

    # _base_xp_reward: float = field(init=False, repr=False)
    # _reward_xp: float = field(init=False, repr=False)
    # _completion_time: float = field(init=False, repr=False)
    # _decay_rate: float = field(init=False, repr=False)
    # # _reward_tier: str = field(init=False, repr=False)
    # _emotional_weight: float = field(init=False, repr=False)


    def __post_init__(self):
        if self.tier is not None and self.tier not in list(range(1,6)): # Our intrinsic tiers from QuestCalculator
            raise ValueError(
                f"Unknown quest tier: {self.tier!r}. "
                f"Expected one of {sorted(self.INTRINSIC_TIER_COSTS)}."
            )
