from pathlib import Path
from typing import Union


def get_project_dir():
    """
    Get the Path to the project/repo directory
    """
    return Path(__file__).parent.parent


def here(relative_sub_path: Union[list, str], project_dir=get_project_dir()):
    """
    Build Paths relative to the root directory
    """
    target_path = project_dir
    if isinstance(relative_sub_path, list):
        for rel_path in relative_sub_path:
            target_path = target_path.joinpath(rel_path)
    else:
        target_path = target_path.joinpath(relative_sub_path)
    return target_path
