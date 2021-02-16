import logging
import os
from enum import Enum

ENV_IDENTIFICATION_VAR_NAME = "DS_PROJECT_ENV"


class InvalidEnvVarSettingException(Exception):
    pass


class DsProjectEnv(Enum):
    dev = 0
    tst = 1
    qas = 2
    prd = 3


def get_env() -> str:
    env = os.getenv(ENV_IDENTIFICATION_VAR_NAME, default=None)
    if env is None:
        logging.warning("Environment variable %s is not set, "
                        "assume running project in 'dev' environment" % ENV_IDENTIFICATION_VAR_NAME)
        env = 'dev'
    elif env not in DsProjectEnv.__members__:
        raise InvalidEnvVarSettingException(
            "Invalid value '{GIVEN_VALUE}' for environment variable '{ENV_VAR}'. "
            "It must be one set to one of the following"
            " {VALID_MEMBERS}".format(
                GIVEN_VALUE=env,
                ENV_VAR=ENV_IDENTIFICATION_VAR_NAME,
                VALID_MEMBERS=list(DsProjectEnv.__members__.keys())
            ))
    else:
        logging.info("Running project in %s environment" % env)

    return env
