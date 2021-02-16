import os
from utils.path import get_project_dir, here
from utils.ident_env import get_env
from utils.load_config import load_config
from utils.logging_setup import get_logger

# build all paths relative to project_dir using here()
project_dir = get_project_dir()
conf_file = here(["conf", "config.yml"])
os.environ['DS_PROJECT_ENV'] = "dev"

# Identify Env via the value of the Environment Variable 'DS_PROJECT_ENV'
env = get_env()
config = load_config(conf_file, env)
logger = get_logger(env, config)

# for debug dependent behaviour (e.g. run script on less data instances)
DEBUG = config.get("debug_default", True)

# logger setup
logger = get_logger(env, config)
logger.debug("Test")
logger.error("Error")

