import datetime
import json
import logging
import os
from typing import Callable, Any

import pandas as pd

from src.utils import get_operations_data_from_excel, data_to_df

logger = logging.getLogger(__name__)

log_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "reports.log")

logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def decorator_spending_by_category(func: Callable) -> Callable:
    """Function decorator writes data to file"""

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs).to_dict(orient='records')

        with open('spending_by_category.json', 'w', encoding="utf-8") as file:
            json.dump(result, file, ensure_ascii=False, indent=4)
        return result

    return wrapper


def writing_data_ro_file(filename: Any) -> Callable:
    """Function decorator writes data to file"""

    def decorator(function: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = function(*args, **kwargs).to_dict(orient='records')

            with open('spending_by_category.json', 'w', encoding="utf-8") as file:
                json.dump(result, file, ensure_ascii=False, indent=4)

            return result

        return wrapper

    return decorator


@decorator_spending_by_category
def spending_by_category(operations: pd.DataFrame, category: str, date: str) -> pd.DataFrame:
    """Function gets all expenses from period"""

    operations_df = operations
    date = pd.to_datetime(date, dayfirst=False)
    start = date - pd.Timedelta(days=90)

    filtered_df = operations_df[
        (pd.to_datetime(operations_df["Дата операции"], dayfirst=True) >= start) &
        (pd.to_datetime(operations_df["Дата операции"], dayfirst=True) <= date)
        ]

    transactions_by_category = filtered_df[filtered_df["Категория"] == category]

    logger.info(f'Returned filtered df by {category}')
    return transactions_by_category


