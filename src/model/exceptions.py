# Base exception for the whole app - lets any caller catch every custom error
# this codebase raises with a single except clause, if they want to.
class DoIkError(Exception):
     """Base class for all custom exceptions in the DoIk Task Manager."""


#Quest-related exceptions

class QuestError(DoIkError):
     """Base class for all quest related exceptions"""

class QuestMissingCategoryError(QuestError):
     """Raised when an operation needs a Quest's category, but none is set."""

class QuestCategoryZeroXP(QuestError):
     """Raised when a Quest's category exists but has 0 XP contribution so far,
    making category-relative calculations (like difficulty) undefined."""