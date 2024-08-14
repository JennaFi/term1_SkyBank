import logging
import os
import re
from typing import List, Dict

from src.utils import get_operations_data_from_excel

logger = logging.getLogger(__name__)

log_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "services.log")

logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def simple_search(operations: List[dict], search_str: str) -> List[Dict]:
    """Function realises simple search by any word in description or category field"""

    pattern = rf'{re.escape(re.sub(r"ть|сти|вать", "", search_str))}?.*'

    for operation in operations:
        operation["category"] = str(operation.get("category"))

    result = [
        operation
        for operation in operations
        if re.search(pattern, operation.get("description", ""), flags=re.IGNORECASE) or
           re.search(pattern, operation.get("category", ""), flags=re.IGNORECASE)
    ]

    logger.info(f'Searched by {search_str}, results are: {result}')
    return result


def search_by_phone_number(operations: List[dict]) -> List[Dict]:
    """Function gets transaction by a phone number."""

    pattern = r'\+7 \d{3} \d{3}-\d{2}-\d{2}|\+7 \d{3} \d{3}-\d{4}'

    result = [
        operation
        for operation in operations
        if re.search(pattern, operation.get("description", ""))
    ]

    logger.info(f'Searched by phone number, results are: {result}')

    return result

