import pandas as pd
import numpy as np
import json
from sensor.config import mongo_client




# we will make a function it will push the file to our monog db this data which id being pushed is being read yb the config file in the same folder
def dump_csv_file_to_mongo_db(file_path:str,database_name:str,collection_name:str):
    data=pd.read_csv(file_path)
    data.reset_index(drop=True,inplace=True)
    json_records=list(json_loads(data.t.to_json()).values())

    mongo_client[database_name][collection_name].insert_many(json_records)
    print("Data Dumped Successfully")