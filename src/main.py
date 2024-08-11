import datetime

import pandas as pd

from src.reports import spending_by_category
from src.services import simple_search, search_by_phone_number
from src.utils import get_user_settings, get_operations_data_from_excel, get_greeting, data_to_df
from src.views import get_main_page_data


def main_page():
    """Main page"""

    user_currencies, user_stocks = get_user_settings()
    greeting = get_greeting()
    transactions = get_operations_data_from_excel("../data/operations.xlsx")

    print(f"""
        {greeting}
        Ваши настройки:
        Курсы валют: {user_currencies}
        Курсы акций: {user_stocks}
        Путь к файлу с транзакциями по умолчанию: "../data/operations.xls"
        Сегодняшняя дата: 31.12.2021
        """
          )

    return transactions


def user_interaction(transactions):
    print(
        """Вам доступны следующие функции:
     
    1. Поиск по указанному слову
    2. Поиск по номерам телефона
    3. Выгрузка трат по выбранной категории за три месяца
     """
    )

    user_choice = input("Выберите функцию: ")

    match user_choice:
        case "1":
            search_string = simple_search(transactions, 'Супер')
            print(search_string)
        case "2":
            search_phone = search_by_phone_number(transactions)
            print(search_phone)
        case "3":

            category = input("Введите категорию: ")

            print(spending_by_category(data_to_df('../data/operations.xlsx'), category, '2021-12-31 15:45:34'))

        case _:
            print("\nОШИБКА ВВОДА! Укажите число 1, 2 или 3")
            user_interaction(transactions)


if __name__ == "__main__":
    sky_bank = main_page()
    user_interaction(sky_bank)
