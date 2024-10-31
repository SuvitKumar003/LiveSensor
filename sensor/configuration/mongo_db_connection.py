from dotenv import load_dotenv
import pymongo
from sensor.constants.database import DATABASE_NAME
import certifi
ca=certifi.where()
from sensor.constants.env_variable import MONGO_URL_KEY
import os
import logging

load_dotenv()

class MongoDBClient:
  client=None

  def __init__(self,database_name=DATABASE_NAME)->None:

       try:

          if MongoDBClient.client is None:
               mongo_db_url=os.getenv(MONGO_URL_KEY)
               logging.info(" Retrive mongo db url i s:{mongo_db_url}")
          else:
                 Mong 
