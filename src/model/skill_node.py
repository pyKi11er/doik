from dataclasses import dataclass, field
from model import Category

@dataclass
class SkillNode:
    node_id: int | None = None
    skill_name: str = ""
    parent_nodes: list = field(default_factory=list)  # list of SkillNode refs - a node
                                                        # can require multiple prior
                                                        # nodes (convergent unlocks)
    description: str = ""
    _embedding_vector: list = field(default_factory=list)
    unlock_xp: int = 0
    category: Category | None = None
    state: int = 0  # 0 = locked, 1 = unlocked, 2 = mastered

    @property
    def embedding_vector(self) -> list:
        return self._embedding_vector.copy()

    @embedding_vector.setter
    def embedding_vector(self, embedding_vector: list):
        self._embedding_vector = embedding_vector.copy() if embedding_vector else []