import logging
import enum
from pathlib import Path
from utils.path import here
from typing import Tuple


class LoggingFileModes(enum.Enum):
    Append = "a"
    OVERWRITE ="w"


def get_formatter():
    return logging.Formatter('%(asctime)s:%(name)s:%(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def get_stream_handler():
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(get_formatter())
    return ch


def get_logger(env: str, config: dict) -> logging.Logger:
    """
    Args:
        env: "dev" | "tst" | "prd"
        config: The config dict as loaded from conf/config.yml

    Returns: The env-specific configured logger object
    """

    # create root logger
    logger = logging.getLogger('')
    logger.setLevel(logging.DEBUG)

    # Add Stream Handler (System I/O)
    if env == "dev":
        stream_handler = get_stream_handler()
        logger.addHandler(stream_handler)

    # Add File Handlers
    info_fh, error_fh = _get_file_handlers(config)
    logger.addHandler(info_fh)
    logger.addHandler(error_fh)

    return logger


def _get_logging_dir_path(config) -> Path:
    conf_log_dir: str = config["logging_dir"]

    # absolute path
    if conf_log_dir.startswith("/"):
        return Path(conf_log_dir)

    # relative path
    else:
        return here(conf_log_dir)


def _create_logging_dir(logging_dir_path: Path):
    logging_dir_path.mkdir(exist_ok=True)


def get_logging_dir_safe(config: dict) -> Path:
    """
    Get the safely existing logging directory path
    Args:
        config: The config dict as loaded from conf/config.yml
    """
    logging_dir_path = _get_logging_dir_path(config)
    if not logging_dir_path.exists():
        _create_logging_dir(logging_dir_path)
    return logging_dir_path


def _get_file_handler_paths(logging_dir_path: Path, config: dict) -> Tuple:
    """
    Args:
        logging_dir_path: The path of the logging directory
        config: The config dict as loaded from conf/config.yml

    Returns: a info_fh_path, error_fh_path tuple
    """
    info_fh_file_name = config["logging_info_name"]
    error_fh_file_name = config["logging_error_name"]
    info_fh_path = logging_dir_path.joinpath(info_fh_file_name)
    error_fh_path = logging_dir_path.joinpath(error_fh_file_name)
    return info_fh_path, error_fh_path


def _get_logging_file_mode(config: dict) -> LoggingFileModes:
    conf_file_mode = config["logging_file_mode"]
    return LoggingFileModes(conf_file_mode)


def _get_file_handlers(config) -> Tuple[logging.FileHandler, logging.FileHandler]:
    """
    Args:
        config: The config object as loaded from conf/config.yml

    Returns: a info_fh, error_fh tuple
    """

    logging_dir = get_logging_dir_safe(config)
    info_path, error_path = _get_file_handler_paths(logging_dir, config)
    file_mode = _get_logging_file_mode(config)
    info_fh = logging.FileHandler(info_path, mode=str(file_mode.value))
    error_fh = logging.FileHandler(error_path, mode=str(file_mode.value))

    # Formatter
    info_fh.setFormatter(get_formatter())
    error_fh.setFormatter(get_formatter())

    # Levels
    info_fh.setLevel(logging.DEBUG)
    error_fh.setLevel(logging.WARN)
    return info_fh, error_fh
