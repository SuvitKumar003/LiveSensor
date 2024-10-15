import sys
import os
## using this file we can not only get the exception but also the line number and the file name where the exception occured also the error message

def error_message_details(error, error_detail: sys):
    # Using sys.exc_info() directly to get the exception details
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = (
        "Error occurred in file [{0}], line number [{1}], error message: [{2}]"
        .format(file_name, exc_tb.tb_lineno, str(error))
    )
    return error_message

class SensorException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)

    def __str__(self):
        return self.error_message
