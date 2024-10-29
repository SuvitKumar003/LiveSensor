from sensor.exception import SensorException
import sys
from sensor.logger import logging  # Ensure this is properly set up in sensor.logger
from sensor.utils import dump_csv_file_to_mongo_db
'''def test_exception():
    try:
        a = 1 / 0
        # Log this as info before the exception occurs (but it won't be reached in this case)
        logging.info("This log won't appear due to zero division error before it.")
    except Exception as e:
        # Log the error in the log file before raising SensorException
        logging.error(f"Error occurred: {e}", exc_info=True)  # exc_info=True logs the traceback
        raise SensorException(e, sys)  # Re-raise the exception with custom error handling

'''
if __name__ == "__main__":
  file_path=file_path = r"dataset\aps_fail_result.csv"

  database_name="sensor_data"
  collection_name="sensor_data_colection"
  dump_csv_file_to_mongo_db(file_path,database_name,collection_name)