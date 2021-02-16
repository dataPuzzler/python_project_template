import logging
import sys
from pathlib import Path
from yaml.scanner import ScannerError
import yaml
from copy import copy
from typing import Union


class UnsetConfigValueException(Exception):
    def __init__(self, unset_keys: list, env: str):
        self.env = env
        self.unset_keys = unset_keys

    def __str__(self):
        return "Unset values for the fields {KEYS} in the '{ENV}' section".format(KEYS=self.unset_keys, ENV=self.env)


def load_config(conf_file: Path, env: str) -> dict:
    config = _parse_config(conf_file, env)
    if not config:
        sys.exit()
    if _validate_config(config, env):
        return config[env]


def _parse_config(conf_file: Path, env: str) -> Union[dict, None]:
    """
    Parse given Config file to dict
    """
    if conf_file.exists():
        with conf_file.open(mode="rt") as f:
            try:
                config = yaml.safe_load(f.read())
                return config
            except ScannerError as e:
                logging.error(" Can not parse the provided config.yml")
                return None
    else:
        raise FileNotFoundError("The expected file conf/config.yml was not found.")


def _validate_config(config: dict, env) -> bool:
    """
    Valid whether all config settings are set
    """
    assert list(config.keys()) == ['default', 'dev', 'tst', 'prd']
    cfg = copy(config['default'])  # default values
    cfg.update(config[env])  # env-specific overwrites
    unset_keys = [k for k, v in cfg.items() if v is None]
    if unset_keys:
        raise UnsetConfigValueException(unset_keys, env)
    return True

