import os
from box.exceptions import BoxValueError
import yaml
from textsummarizer.logging import logger
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path
from typing import Type


@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories :list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list):  list of path of directories
        ignore_log (bool, optionsl): ignore if multiple directories to be created . defaults to false
    """
    for path in path_to_directories:
         os.makedirs(path, exist_ok= True)
         if verbose:
             logger.info(f"Creating Directory at : {path}")



@ensure_annotations
def get_size(path: Path)-> str:
    """"
    get size in kb

    Args:
        path (Path):  path of the file

        Returns:
        str: size in kb
        """
    
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"
    