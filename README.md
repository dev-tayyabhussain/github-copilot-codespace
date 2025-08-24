# Documentation for util functions

This directory contains utility functions that are used across various parts of the project. These functions are designed to perform common tasks and operations, making it easier to maintain and reuse code.

## Overview of Utility Functions

The utility functions are organized into several categories based on their functionality:

1. **String Utilities**: Functions for manipulating and processing strings.
2. **Array Utilities**: Functions for handling arrays and collections.
3. **Date Utilities**: Functions for working with dates and times.
4. **Math Utilities**: Functions for performing mathematical calculations.
5. **File Utilities**: Functions for file operations such as reading, writing, and manipulating
6. **Network Utilities**: Functions for handling network requests and responses.
7. **Validation Utilities**: Functions for validating data and inputs.
8. **Logging Utilities**: Functions for logging and debugging information.


## How to Use the Utility Functions

1. **String Utilities**

to_camel_case(s: str) -> str
Converts a string to camelCase format.

reverse_words(sentence: str) -> str
Reverses the order of words in a sentence.

2. **Array Utilities**

flatten_array(nested: List[Any]) -> List[Any]
Flattens a nested list into a single list.

chunk_array(arr: List[Any], size: int) -> List[List[Any]]
Splits a list into chunks of the given size.

3. **Date Utilities**

days_between(date1: str, date2: str, fmt="%Y-%m-%d") -> int
Returns the number of days between two dates.

add_days(date_str: str, days: int, fmt="%Y-%m-%d") -> str
Adds a number of days to a date and returns the new date as a string.

4. **Math Utilities**

is_prime(n: int) -> bool
Checks if a number is prime.

factorial(n: int) -> int
Returns the factorial of a number using recursion.

5. **File Utilities**

read_file(file_path: str) -> str
Reads the contents of a file and returns it as a string.

copy_file(src: str, dest: str) -> None
Copies a file from source to destination.

6. **Network Utilities**

get_ip_address() -> str
Returns the local machine's IP address.

fetch_url(url: str, timeout: int = 5) -> Union[str, None]
Sends a GET request to the URL and returns the response text.

7. **Validation Utilities**

is_valid_email(email: str) -> bool
Validates if a string is in email format.

is_json(my_str: str) -> bool
Checks if a string is a valid JSON.

8. **Logging Utilities**

setup_logger(name: str, level=logging.DEBUG, file: str = None)
Sets up and returns a configured logger.

log_debug(logger, message: str)
Logs a debug-level message using the provided logger.
