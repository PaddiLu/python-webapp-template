"""
Module for parsing a config file.
"""

import tomllib

from . import const


def _evaluate_loaded_config(config: dict, default: dict) -> dict:
    """
    Parses a loaded config in dict form,
    replacing keys from the config file with internal keys.
    Inserts default values where values are missing.
    """
    out = {}
    for key in default.keys():
        mappedkey = const.config.KEYS.get(key, key)
        if mappedkey not in config or config[mappedkey] is default[key]:
            out[key] = default[key]
        elif isinstance(default[key], dict):
            out[key] = _evaluate_loaded_config(config[mappedkey], default[key])
        else:
            out[key] = config[mappedkey]
    return out

def fetch() -> dict:
    """
    Loads and parses the config file,
    substituting default values for missing keys.

    Returns the default config if the config file is unavailable.
    """

    from .paths import CONFIG as configpath

    try:
        with open(configpath, 'rb') as f:
            config = tomllib.load(f)
    except(FileNotFoundError, IsADirectoryError, PermissionError):
        return const.config.DEFAULT
    
    # Substitute missing values with defaults
    out = _evaluate_loaded_config(config, const.config.DEFAULT)

    return out
