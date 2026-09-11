from dataclasses import dataclass, field
from datetime import datetime
from model import Character

# A daily log class for logging sleep hours, meals, and mood.
# This will be used to determine the xp contribution for the questline and category
# in the future, also will affect stamina and focus.
@dataclass
class Log:
    log_id: int | None = None
    ref_to_character: Character | None = None
    timestamp: datetime = field(default_factory=datetime.now)
    sleep_hours: float = 0
    meal_quality: int | None = None
    mood: int | None = None