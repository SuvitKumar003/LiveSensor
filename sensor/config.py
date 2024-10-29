from dataclasses import dataclass
import os
import pymongo
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Load environment variables from .env file
load_dotenv()

@dataclass
class EnvironmentVariable:
    mongo_username: str = os.getenv("MONGO_USERNAME")
    mongo_password: str = os.getenv("MONGO_PASSWORD")
    mongo_cluster: str = os.getenv("MONGO_CLUSTER")

    def get_mongo_uri(self):
        if not (self.mongo_username and self.mongo_password and self.mongo_cluster):
            raise ValueError("Environment variables for MongoDB connection are not set correctly.")
        
        # Encode username and password
        username = quote_plus(self.mongo_username)
        password = quote_plus(self.mongo_password)

        # Construct the MongoDB URI
        mongo_uri = f"mongodb+srv://{username}:{password}@{self.mongo_cluster}/?retryWrites=true&w=majority"
        return mongo_uri

# Initialize the MongoDB client with the constructed URI
env_vars = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_vars.get_mongo_uri())
