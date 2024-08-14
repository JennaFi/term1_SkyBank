import json
import logging
import os


from src.external_api import get_exchange_rates, get_stock_prices, api_key, api_key_stock, symbols
from src.utils import (get_operations_data_from_excel,
                       get_greeting, get_cards_numbers,
                       get_sum_expenses_by_card,
                       get_top_5_transactions,
                       get_cashback_by_card)

logger = logging.getLogger(__name__)

log_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "views.log")

logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_main_page_data(date: str) -> str:
    """Gets all the data for main page"""

    operations = get_operations_data_from_excel('../data/operations.xlsx')
    greeting = get_greeting()
    cards = get_cards_numbers(operations)
    expenses = get_sum_expenses_by_card(operations, date)
    top_transactions = get_top_5_transactions(operations, date)
    cashback = get_cashback_by_card(operations, date)
    currency_rates = get_exchange_rates(api_key)
    stock_prices = get_stock_prices(api_key_stock, symbols)

    main_page_dict = {"greeting": greeting, "cards": cards, "expenses": expenses, "top_transactions": top_transactions,
                      "cashback": cashback, "currency_rates": currency_rates, "stock_prices": stock_prices}

    main_dict_json = json.dumps(main_page_dict, indent=4, ensure_ascii=False)
    with open('main_dict_.json', 'w', encoding="utf-8") as file:
        json.dump(main_page_dict, file, ensure_ascii=False, indent=4)
    logger.info(f"Writing down jsonfile {main_page_dict}")

    return main_dict_json


# print(get_main_page_data('31.12.2021'))

