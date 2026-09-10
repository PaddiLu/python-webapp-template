#!/usr/bin/env python3

"""
Script for writing a default config to STDOUT.
"""

import os.path
import sys

ROOT = (os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ROOT)

from app.config import generate_toml
from app.const import config

print(generate_toml(config.DEFAULT))

