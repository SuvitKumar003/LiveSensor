from sensor.exception import SensorException
import sys
from sensor.logger import logging  # Ensure this is properly set up in sensor.logger

def test_exception():
    try:
        a = 1 / 0
        # Log this as info before the exception occurs (but it won't be reached in this case)
        logging.info("This log won't appear due to zero division error before it.")
    except Exception as e:
        # Log the error in the log file before raising SensorException
        logging.error(f"Error occurred: {e}", exc_info=True)  # exc_info=True logs the traceback
        raise SensorException(e, sys)  # Re-raise the exception with custom error handling

if __name__ == "__main__":
    try:
        test_exception()
    except SensorException as e:
        print(e)  # Print the exception message to the console
