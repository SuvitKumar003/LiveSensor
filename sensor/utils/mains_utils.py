import yaml
import os
import logging
import pandas as pd
import numpy as np
from sensor.exceptions import SensorError

def read_yaml(file_path:str)->dict:
    """
    Read the yaml file and return the dictionary
    """
    try:
        with open(file_path, "rb") as yaml_file:
           return yaml.safe_load(yaml_file)
    except Exception as e:
        logging.error(f"Error reading the yaml file: {e}")
        raise SensorError(f"Error reading the yaml file: {e}")
    

def write_yaml(file_path:str,content:object,replace:bool=False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
            os.makedirs(os.path.dirname(file_path),exist_ok=True)
            with open(file_path,"w") as file:
                yaml.dump(content,file)
    except Exception as e:
        raise SensorError(e,sys)
    