import sys

def handle_exception(error, error_detail:sys):
    # This gets information about WHERE the error happened
    _, _, exc_tb = error_detail.exc_info()
    
    # Extract the line number where error occurred
    line_number = exc_tb.tb_lineno
    
    # Extract the file name where error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Create a nice, readable error message
    error_message = f"Error occurred in script: {file_name} at line: {line_number} with message: {str(error)}"
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)  # Call parent Exception class
        # Store the formatted error message
        self.error_message = handle_exception(error_message, error_detail)
    
    def __str__(self):
        # When you print this exception, show the formatted message
        return self.error_message