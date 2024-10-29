from dataclasses import dataclass
import os
import pymongo
import urllib.parse

@dataclass
class EnvironmentVariable:
    mongo_db_url: str = os.getenv("MONGO_DB_URL")

# Ensure special characters are URL-encoded
url = EnvironmentVariable().mongo_db_url
if url:
    mongo_client = pymongo.MongoClient(url)
else:
    raise ValueError("MONGO_DB_URL environment variable is not set or empty.")
