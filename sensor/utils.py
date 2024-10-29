import pandas as pd
import json
from sensor.config import mongo_client  # Import mongo_client from config.py

def dump_csv_file_to_mongo_db(file_path: str, database_name: str, collection_name: str):
    # Read the CSV file
    data = pd.read_csv(file_path)
    data.reset_index(drop=True, inplace=True)
    
    # Convert to JSON
    json_records = json.loads(data.to_json(orient='records'))

    # Insert JSON records into MongoDB
    mongo_client[database_name][collection_name].insert_many(json_records)
    print("Data Dumped Successfully")
