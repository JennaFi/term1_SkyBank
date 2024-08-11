import json
import os
from typing import List, Dict

import pandas as pd
import datetime
import logging

date_now = datetime.datetime.now().date().strftime('%d.%m.%Y')
# month_year = date_now[3:5] + date_now[6:]

logger = logging.getLogger(__name__)

log_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "utils.log")

logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_greeting() -> str:
    """Greeting function"""
    current_time = datetime.datetime.now().hour
    if 5.00 <= current_time < 12.00:
        return f'Доброе утро!'
    if 12.00 <= current_time < 17.00:
        return f'Добрый день!'
    if 17.00 <= current_time < 21.00:
        return f'Добрый вечер!'
    else:
        return f'Доброй ночи!'


def get_operations_data_from_excel(file_path: str) -> List[dict]:
    """Function returns info about financial transactions from Excel-file in JSON-format."""
    try:
        df = pd.read_excel(file_path)
        operations_dict = df.fillna(0).to_dict(orient="records")
        formatted_dict = [
            {
                "operation_date": (i.get("Дата операции")),
                "payment_date": i.get("Дата платежа"),
                "card_number": i.get("Номер карты"),
                "status": i.get("Статус"),
                "sum_operation": i.get("Сумма операции"),
                "currency_operation": i.get("Валюта операции"),
                "payment_sum": i.get("Сумма платежа"),
                "payment_currency": i.get("Валюта платежа"),
                "cashback": i.get("Кэшбэк"),
                "category": i.get("Категория"),
                "MCC": i.get("MCC"),
                "description": i.get("Описание"),
                "bonus": i.get("Бонусы (включая кэшбэк)"),
                "invest_bank": i.get("Округление на инвесткопилку"),
                "rounded_operation_sum": i.get("Сумма операции с округлением"),
            }
            for i in operations_dict
        ]

        logger.info('File changed to json')
        with open('xlsx_to_json.json', 'w', encoding="utf-8") as file:
            json.dump(formatted_dict, file, ensure_ascii=False, indent=4)
        return formatted_dict

    except FileNotFoundError:
        return []


def data_to_df(file_path: str):
    """Turns excel file data to dataframe"""
    df = pd.read_excel(file_path)
    logger.info("File changed to DataFrame")

    return df


def get_cards_numbers(operations: List[dict]) -> List:
    """Function gets list of all cards"""

    cards_list = list({operation.get("card_number") for operation in operations
                       if isinstance(operation.get("card_number"), str)})
    logger.info(f'List of cards: {cards_list}')
    return cards_list


# print(get_cards_numbers((get_operations_data_from_excel('../data/operations.xlsx'))))


def get_sum_expenses_by_card(operations: List[dict], month_year: str) -> List[Dict]:
    """Function gets all expenses by every card"""

    cards_expenses = {}

    for operation in operations:
        card_number = operation.get("card_number")
        date = str(operation.get("payment_date"))

        if operation["card_number"] == card_number and date[3:] == month_year[3:]:
            if card_number not in cards_expenses:
                cards_expenses[card_number] = 0
                cards_expenses[card_number] += operation.get("payment_sum")
    result = [
        {"card_number": card_number, "all_payments": round(abs(all_payments), 2)} for card_number,
        all_payments in cards_expenses.items()
    ]
    logger.info(f'Expences by card: {result} ')

    return result


def get_cashback_by_card(operations: List[dict], month_year: str) -> List[Dict]:
    """Function gets cashback by every card"""

    cashback = {}

    for operation in operations:
        card_number = operation.get("card_number")
        date = str(operation.get("payment_date"))

        if isinstance(card_number, str) and date[3:] == month_year[3:]:
            if card_number not in cashback:
                cashback[card_number] = 0.0
            cashback[card_number] += (operation.get("payment_sum") / 100)
    result = [{"card_number": card_number, "cashback": round(abs(cashback), 2)} for card_number,
    cashback in cashback.items()]
    logger.info(f'Cashback by cards: {result}')
    return result


def get_top_5_transactions(operations: List[dict], month_year: str) -> List[Dict]:
    """Function gets TOP 5 transactions"""

    transactions = {}

    for operation in operations:
        date = str(operation.get("payment_date"))
        transaction = abs(operation.get("payment_sum"))
        description = operation.get("description")

        if date[3:] == month_year[3:]:
            transactions[transaction] = description

    transactions_list = sorted(
        [{"transaction": transaction, "description": description} for transaction, description in transactions.items()],
        key=lambda x: x["transaction"], reverse=True)
    logger.info(f'TOP-5 transactions are: {transactions_list[:5]}')
    return transactions_list[:5]


def get_current_month_operations(operations: pd.DataFrame, date: str) -> pd.DataFrame:
    """Gets data for specified dates"""

    end_date = pd.to_datetime(date, dayfirst=False)
    start_date = end_date - pd.Timedelta(days=90)
    end_date = end_date.replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)
    month_operations = operations.loc[
        (operations["Дата операции"] <= end_date) & (operations["Дата операции"] >= start_date)
        ]
    return month_operations


def get_user_settings(path='../user_settings.json/') -> tuple:
    """Gets user settings in currencies and stocks"""

    with open(path) as file:
        user_settings = json.load(file)
        logger.info(f"User settings are: {user_settings}")
    return user_settings["user_currencies"], user_settings["user_stocks"]
