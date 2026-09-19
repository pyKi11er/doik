from __future__ import annotations
from dataclasses import dataclass, field
from model import Category

@dataclass
class SkillTree:    
    tree_id: int | None = None
    ref_to_cat: Category | None = None
    child_nodes: list = field(default_factory=list)
    unlocked_nodes: list = field(default_factory=list)
    locked_nodes: list = field(default_factory=list)
    tree_name: str = ""
    tree_lvl: int = 1
    total_xp: float = 0