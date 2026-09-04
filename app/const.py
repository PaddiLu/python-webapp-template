"""
Provides constants used across this app.
"""

from abc import ABC
from typing import final


@final
class directories(ABC):
    STATIC = 'static'
    TEMPLATES = 'templates'

@final
class env(ABC):
    """Names of environmental variables"""
    _APPNAME = 'WEBAPP'

    CONFIGPATH = ''.join((_APPNAME, '_CONFIG_PATH'))

@final
class config(ABC):
    """Keys and default values for the config file."""

    DEFAULT = {
        # Nested dictionary containing default config
    }

    KEYS = {
        # Maps keys used in config dictionaries
        # to keys used in config file
    }

    TOML_HEADER = '# This is a TOML config file'
    TOML_VALID_KEY_REGEX = '^[A-Za-z0-9_-]+$'

    TABLES: tuple[tuple[str, ...], ...] = (
        # These keys will be used as headers in the TOML file
    )
