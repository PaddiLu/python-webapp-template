"""
Provides constants used across this app.
"""

from abc import ABC
from typing import final


@final
class app(ABC):
    """Information about this app."""
    NAME = 'Python Webapp Template'

@final
class directories(ABC):
    STATIC = 'static'
    TEMPLATES = 'templates'

@final
class env(ABC):
    """Names of environmental variables"""

    pass
