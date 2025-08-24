import os
import re
import math
import json
import shutil
import socket
import logging
import requests
from datetime import datetime, timedelta
from typing import List, Any, Union


# 1. STRING UTILITIES
def to_camel_case(s: str) -> str:
    parts = re.split(r'[\s_\-]+', s)
    return parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])


def reverse_words(sentence: str) -> str:
    return ' '.join(reversed(sentence.strip().split()))


# 2. ARRAY UTILITIES
def flatten_array(nested: List[Any]) -> List[Any]:
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_array(item))
        else:
            result.append(item)
    return result


def chunk_array(arr: List[Any], size: int) -> List[List[Any]]:
    return [arr[i:i + size] for i in range(0, len(arr), size)]


# 3. DATE UTILITIES
def days_between(date1: str, date2: str, fmt="%Y-%m-%d") -> int:
    d1 = datetime.strptime(date1, fmt)
    d2 = datetime.strptime(date2, fmt)
    return abs((d2 - d1).days)


def add_days(date_str: str, days: int, fmt="%Y-%m-%d") -> str:
    date = datetime.strptime(date_str, fmt)
    new_date = date + timedelta(days=days)
    return new_date.strftime(fmt)


# 4. MATH UTILITIES
def is_prime(n: int) -> bool:
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n - 1)


# 5. FILE UTILITIES
def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def copy_file(src: str, dest: str) -> None:
    shutil.copy2(src, dest)


# 6. NETWORK UTILITIES
def get_ip_address() -> str:
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except Exception as e:
        return f"Error: {e}"


def fetch_url(url: str, timeout: int = 5) -> Union[str, None]:
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"Error: {e}"


# 7. VALIDATION UTILITIES
def is_valid_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def is_json(my_str: str) -> bool:
    try:
        json.loads(my_str)
        return True
    except ValueError:
        return False


# 8. LOGGING UTILITIES
def setup_logger(name: str = 'app_logger', level=logging.DEBUG, file: str = None):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if file:
        file_handler = logging.FileHandler(file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def log_debug(logger, message: str):
    logger.debug(message)