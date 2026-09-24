# Base exception for the whole app - lets any caller catch every custom error
# this codebase raises with a single except clause, if they want to.
class DoIkError(Exception):
     """Base class for all custom exceptions in the DoIk Task Manager."""


#Quest-related exceptions

class QuestError(DoIkError):
    """Base class for any error raised while working with a Quest."""
 
 
class QuestMissingCategoryError(QuestError):
    """Raised when an operation needs a Quest's category, but none is set."""
 
 
class QuestMissingSkillTreeError(QuestError):
    """Raised when calculateDifficulty is called without the SkillTree that
    corresponds to the quest's category."""


class QuestMissingCharacterError(QuestError):
    """Raised when calculateDifficulty is called without the Character reference"""
 
 
class QuestInvalidSkillTreeLevelError(QuestError):
    """Raised when the provided SkillTree has a non-positive tree_lvl, which
    would make difficulty (100 / tree_lvl) undefined."""


class QuestIsNone(QuestError):
    """Raised from calculator when passing a None quest for calculating difficulty or reward"""

#Character-related exceptions

class CharacterError(DoIkError):
    """Base class for any error raised while working with a Character."""

class CharacterSkillForestAlreadyExists(CharacterError):
    """Raised when trying to force a reference change for skill forest in character"""


class CharacterMissingSkillForestError(CharacterError):
    """Raised when a calculation needs a Character's SkillForest, but none has
    been assigned yet - expected for a freshly-created Character."""