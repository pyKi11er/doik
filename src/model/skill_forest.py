# Holds the top-level collection of per-category SkillTrees. Still worth deciding
# whether this needs to be a real persisted class, it currently carries no state
# beyond a plain list, so it could just as easily be an implicit query at the
# app/service level rather than an entity of its own.
from dataclasses import dataclass, field

@dataclass
class SkillForest:
    tree_arr: list = field(default_factory=list)

    def addTree(self, tree):
        self.tree_arr.append(tree)