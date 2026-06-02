"""
Provides constants used across this app.
"""

from abc import ABC
from os import environ
from typing import final

@final
class directories(ABC):
    STATIC = 'static'
    TEMPLATES = 'templates'
