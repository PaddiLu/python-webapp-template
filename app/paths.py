"""
Provides paths to files and directories.
"""

from os import path

from . import const

ROOT = path.normpath (path.join(path.dirname(__file__), '..'))
STATIC = path.join (ROOT, const.directories.STATIC)
TEMPLATES = path.join (ROOT, const.directories.TEMPLATES)
