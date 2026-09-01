"""
Provides paths to files and directories.
"""

from os import environ, path

from . import const


ROOT = path.normpath (path.join(path.dirname(__file__), '..'))
STATIC = path.join (ROOT, const.directories.STATIC)
TEMPLATES = path.join (ROOT, const.directories.TEMPLATES)

_CONFIG_DEFAULT = path.join(ROOT, 'CONFIG.toml')
CONFIG = environ.get(const.env.CONFIGPATH, _CONFIG_DEFAULT)
