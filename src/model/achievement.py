from dataclasses import dataclass, field
from datetime import datetime

# A class for achievements that the user can unlock based on their progress in the app,
# or for streak milestones.
@dataclass
class Achievement:
    achievement_id: int | None = None
    achievement_name: str = ""
    achievement_desc: str = ""
    achievement_date: datetime = field(default_factory=datetime.now)
    streak_milestone: int | None = None