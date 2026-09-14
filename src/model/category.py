from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Category:
    category_id: int | None = None
    cat_name: str = ""
    cat_desc: str = ""
    color: str | None = None
    parent_cat: Category | None = None  # None => this is one of the 5 core categories

    #Will determine category based on category_id if category_id between
    #0-5 then parent_category is null if category_id is above that
    #will use an algorithm to determine the parent category and assign the id
    # of the parent
    def determineCoreCategory(self):
        ...