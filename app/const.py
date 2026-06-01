"""
Provides constants used across this app.
"""

from abc import ABC
from os import environ
from typing import final

@final
class app(ABC):
    """Information about this app."""
    NAME = 'Python Web App Template'

@final
class directories(ABC):
    STATIC = 'static'
    TEMPLATES = 'templates'
