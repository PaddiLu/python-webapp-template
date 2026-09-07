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

def generate_toml(config: dict) -> str:
    """
    Generates the contents of a TOML config
    from a config in dictionary form.
    """
    import datetime as dt
    from numbers import Number
    from re import compile as compile_regex
    import typing

    KEY_VALIDATOR = compile_regex(const.config.TOML_VALID_KEY_REGEX)

    def _get_config_key(setting: str) -> str:
        """Get the key to use for setting in TOML"""
        result = const.config.KEYS.get(setting, setting)
        if not bool(KEY_VALIDATOR.match(result)):
            # Keys with invalid characters must be quoted
            result = ''.join(('"', result, '"'))
        return result

    def _setting_to_str(setting: tuple[str, ...], value: typing.Any) -> str:
        """Return setting formatted for TOML"""
        key = '.'.join((_get_config_key(s) for s in setting))
        if isinstance(value, bool):
            formatted_value = 'true' if value else 'false'
        elif isinstance(value, (dt.datetime, dt.date, dt.time)):
            formatted_value = value.isoformat()
        elif isinstance(value, Number):
            formatted_value = str(value)
        elif isinstance(value,(list,tuple)):
            value = str([_setting_to_str(item) for item in value])
        else: # Treat as string
            formatted_value = str(value)
            for char, escape in const.config.TOML_ESCAPE_CHAR_MAP:
                if char in formatted_value:
                    formatted_value = formatted_value.replace(char, escape)
            if '\n' in formatted_value:
                formatted_value = ''.join(('"""\n', formatted_value, '"""'))
            else:
                formatted_value = ''.join(('"', formatted_value, '"'))
        return(' '.join((key, '=', formatted_value)))

    def _evaluate_group(contents: dict, group: tuple[str, ...] = (), table: tuple[str, ...] = ()) -> tuple[list[str],list[tuple[tuple[str, ...], list[str]]]]:
        """Convert dict to list of settings recursively"""

        top_level_settings = []
        grouped_settings = []
        subtables: list[tuple[tuple[str, ...], list[str]]] = []

        for key, value in contents.items():
            group_key = (*group, key)
            if isinstance(value, dict):
                full_key = table + group_key
                if full_key in const.config.TABLES:
                    # This is a seperate table
                    new_table, new_subtables = _evaluate_group(value, table=full_key)
                    subtables.append((full_key, new_table))
                    subtables.extend(new_subtables)
                else:
                    # Subgroup of settings for current table
                    new_settings, new_subtables = _evaluate_group(value, group_key)
                    grouped_settings.extend(new_settings)
                    subtables.extend(new_subtables)
            else:
                # New setting for current group
                top_level_settings.append(_setting_to_str(group_key, value))
        return (top_level_settings + grouped_settings), subtables

    # Evaluate config; generate tables as lists
    top_level_settings, tables = _evaluate_group(config)
    if top_level_settings:
        tables = (((), top_level_settings), *tables)
    # Format as TOML
    text_blocks = [const.config.TOML_HEADER]
    for group, content in tables:
        if group:
            key = '.'.join((_get_config_key(s) for s in group))
            header = ''.join(('[', key, ']'))
            content = (header, *content)
        text_blocks.append('\n'.join(content))
    return '\n\n'.join(text_blocks)

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
