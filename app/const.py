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
    TOML_ESCAPE_CHAR_MAP = (
        ('\\','\\\\'), ('"', '\\"'), ('\t', '\\t'), ('\f', '\\f'),
        ('\b', '\\b'), ('\r', '\\r'), ('\x00', '\\u0000'),
        ('\x01', '\\u0001'), ('\x02', '\\u0002'), ('\x03', '\\u0003'),
        ('\x04', '\\u0004'), ('\x05', '\\u0005'), ('\x06', '\\u0006'),
        ('\x07', '\\u0007'), ('\x0b', '\\u000B'), ('\x0e', '\\u000E'),
        ('\x0f', '\\u000F'), ('\x10', '\\u0010'), ('\x11', '\\u0011'),
        ('\x12', '\\u0012'), ('\x13', '\\u0013'), ('\x14', '\\u0014'),
        ('\x15', '\\u0015'), ('\x16', '\\u0016'), ('\x17', '\\u0017'),
        ('\x18', '\\u0018'), ('\x19', '\\u0019'), ('\x1a', '\\u001A'),
        ('\x1b', '\\u001B'), ('\x1c', '\\u001C'), ('\x1d', '\\u001D'),
        ('\x1e', '\\u001E'), ('\x1f', '\\u001F'), ('\x7f', '\\u007F'),
    )

    TABLES: tuple[tuple[str, ...], ...] = (
        # These keys will be used as headers in the TOML file
    )
