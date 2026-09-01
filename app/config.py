"""
Module for parsing a config file.
"""

import tomllib

from . import const


# Global variables
_cached_config = const.config.DEFAULT
_caching_timestamp = None


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

    from os.path import getmtime

    from .paths import CONFIG as configpath

    global _cached_config, _caching_timestamp

    try:
        file_timestamp = getmtime(configpath)
        if file_timestamp == _caching_timestamp:
            # Return cached config if cache is up to date
            return _cached_config
        with open(configpath, 'rb') as f:
            config = tomllib.load(f)
    except(FileNotFoundError, IsADirectoryError, PermissionError):
        return const.config.DEFAULT
    
    # Substitute missing values with defaults
    _cached_config = _evaluate_loaded_config(config, const.config.DEFAULT)
    _caching_timestamp = file_timestamp

    return _cached_config
