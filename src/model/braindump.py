from dataclasses import dataclass, field
from datetime import datetime
from model import Questline

#A class for future implementation a lanuage model
# for determining the user's current sitation and generate
# quests for him.
@dataclass
class BrainDump:
    brain_dump_id: int | None = None
    text: str = ""
    timestamp: datetime = field(default_factory=datetime.now)
    embedding_vector: list = field(default_factory=list)
    ref_to_questline: Questline | None = None