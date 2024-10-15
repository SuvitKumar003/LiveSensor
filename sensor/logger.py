import logging
import sys
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S') }.log"
 
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
#this lie is going to  make the folder wiht name logger this will make only if no folder exist if it already exist then this command will be skipped
os.makedirs(log_path,exist_ok=True)
log_file_path=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
  filename=log_file_path,
  format="[ %(asctime)s]  %(lineno)d  %(name)s - %(levelname)s - %(message)s",
  level=logging.INFO
)

#class Logger:

