#  - Here we will have functions for saving and loading:
# 1. json files (save and load)
# 2. yaml files (load only)
# 3. binary files (i.e. models and preprocessors) as pickle files (save and load)


# - We will also create directories whevever required

# - Get size of file is also coded here

import os
import yaml
import joblib
import json

from pathlib import Path #type: ignore
from src.mlproject import logger
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from box import ConfigBox


@ensure_annotations
def load_yaml(file:Path) -> ConfigBox:
    try:
        with open(file) as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("The YAML file: {0} is loaded".format(file))
            return ConfigBox(config)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    
    except Exception as e:
        raise e

@ensure_annotations
def save_json(data: dict, path: Path):
    with open(path,'w') as json_file:
        json.dump(data,json_file)
        logger.info("JSON file is saved at".format(path))

@ensure_annotations
def load_json(path:Path)->ConfigBox:
    with open(path) as json_file:
        content = json.load(json_file)
        logger.info(f"JSON file from {path} is loaded")
    return(ConfigBox(content))

@ensure_annotations
def save_binary(object,path:Path):
    joblib.dump(value= object, filename= path)
    logger.info("File pickled at {0}".format(path))

@ensure_annotations
def load_binary(path:Path):
    object = joblib.load(path)
    logger.info(f"Object loaded from {path}")
    return(object)

def create_directories(dir):
    os.makedirs(dir,exist_ok=True)
    logger.info("Directory:{0} is created".format(dir))

@ensure_annotations
def get_size(path: Path) ->str:
    size = round(os.path.getsize(path)/1024)
    return(f"~ {size} KB")


# @ensure_annotations >> this is given so that:
# whenever a method in this file is called from a main program, @ensure_annotations will ensure that
# the input datatype for the arguement of the fuction is same as mentioned in the method definition
# suppose: def product(x:int,y:int)->int:
#               return(x*y)
# If we call this function like: 
#           product (x = 4, y = "7")
# Without @ensure_annotations, the above function will return: 7777
# 
# However, we want 28. To do that, we will define the method as:
# @ensure_annotations
# def product(x:int,y:int)->int:
#   return(x*y) 
# 
# This will ensure that x and y are being input as integers only. 


# ConfigBox will make the key-value pairs of a dictionaries accessible easily like attributes.
# for eg. d = {"key":"value"}
# 
# To access the dictionary, we have to write:
# d['key']
#
# However using ConfigBox, it becomes easy:
# d1 = ConfigBox({"key":"Value"})
# d1.key >>"Value"
