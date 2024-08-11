import pandas as pd
import pytest
from pandas import Timestamp


@pytest.fixture
def file_path():
    return '../data/operations.xlsx'


@pytest.fixture
def month_year():
    return "31.12.2021"


@pytest.fixture
def search_str():
    return "Супермаркеты"


@pytest.fixture
def operations():
    return [
        {
            "operation_date": "31.12.2021 16:44:00",
            "payment_date": "31.12.2021",
            "card_number": "*7197",
            "status": "OK",
            "sum_operation": -160.89,
            "currency_operation": "RUB",
            "payment_sum": -160.89,
            "payment_currency": "RUB",
            "cashback": 0.0,
            "category": "Супермаркеты",
            "MCC": 5411.0,
            "description": "Колхоз",
            "bonus": 3,
            "invest_bank": 0,
            "rounded_operation_sum": 160.89
        },
        {
            "operation_date": "31.12.2021 16:42:04",
            "payment_date": "31.12.2021",
            "card_number": "*7197",
            "status": "OK",
            "sum_operation": -64.0,
            "currency_operation": "RUB",
            "payment_sum": -64.0,
            "payment_currency": "RUB",
            "cashback": 0.0,
            "category": "Супермаркеты",
            "MCC": 5411.0,
            "description": "Колхоз",
            "bonus": 1,
            "invest_bank": 0,
            "rounded_operation_sum": 64.0
        },
        {
            "operation_date": "31.12.2021 16:39:04",
            "payment_date": "31.12.2021",
            "card_number": "*7197",
            "status": "OK",
            "sum_operation": -118.12,
            "currency_operation": "RUB",
            "payment_sum": -118.12,
            "payment_currency": "RUB",
            "cashback": 0.0,
            "category": "Супермаркеты",
            "MCC": 5411.0,
            "description": "Магнит",
            "bonus": 2,
            "invest_bank": 0,
            "rounded_operation_sum": 118.12
        },
        {
            "operation_date": "31.12.2021 15:44:39",
            "payment_date": "31.12.2021",
            "card_number": "*7197",
            "status": "OK",
            "sum_operation": -78.05,
            "currency_operation": "RUB",
            "payment_sum": -78.05,
            "payment_currency": "RUB",
            "cashback": 0.0,
            "category": "Супермаркеты",
            "MCC": 5411.0,
            "description": "Колхоз",
            "bonus": 1,
            "invest_bank": 0,
            "rounded_operation_sum": 78.05
        },
        {
            "operation_date": "31.12.2021 01:23:42",
            "payment_date": "31.12.2021",
            "card_number": "*5091",
            "status": "OK",
            "sum_operation": -564.0,
            "currency_operation": "RUB",
            "payment_sum": -564.0,
            "payment_currency": "RUB",
            "cashback": 0.0,
            "category": "Различные товары",
            "MCC": 5399.0,
            "description": "Ozon.ru",
            "bonus": 5,
            "invest_bank": 0,
            "rounded_operation_sum": 564.0
        },
        {
            "operation_date": "31.12.2021 00:12:53",
            "payment_date": "31.12.2021",
            "card_number": 0,
            "status": "OK",
            "sum_operation": -800.0,
            "currency_operation": "RUB",
            "payment_sum": -800.0,
            "payment_currency": "RUB",
            "cashback": 0.0,
            "category": "Переводы",
            "MCC": 0.0,
            "description": "Константин Л.",
            "bonus": 0,
            "invest_bank": 0,
            "rounded_operation_sum": 800.0
        }
    ]


@pytest.fixture
def operations_phone():
    return [

        {'operation_date': '18.11.2021 21:15:27',
         'payment_date': '19.11.2021',
         'card_number': 0,
         'status': 'OK',
         'sum_operation': -200.0,
         'currency_operation': 'RUB',
         'payment_sum': -200.0,
         'payment_currency': 'RUB',
         'cashback': 0.0,
         'category': 'Мобильная связь',
         'MCC': 0.0,
         'description': 'Тинькофф Мобайл +7 995 555-55-55',
         'bonus': 2,
         'invest_bank': 0,
         'rounded_operation_sum': 200.0
         },

        {'operation_date': '18.11.2021 21:15:27',
         'payment_date': '19.11.2021',
         'card_number': 0,
         'status': 'OK',
         'sum_operation': 200.0,
         'currency_operation': 'RUB',
         'payment_sum': 200.0,
         'payment_currency': 'RUB',
         'cashback': 0.0,
         'category': 'Пополнения',
         'MCC': 0.0,
         'description': 'Тинькофф Мобайл +7 995 555-55-55',
         'bonus': 0,
         'invest_bank': 0,
         'rounded_operation_sum': 200.0
         },
        {'operation_date': '14.03.2021 09:49:03',
         'payment_date': '14.03.2021',
         'card_number': 0,
         'status': 'OK',
         'sum_operation': -150.0,
         'currency_operation': 'RUB',
         'payment_sum': -150.0,
         'payment_currency': 'RUB',
         'cashback': 0.0,
         'category': 'Мобильная связь',
         'MCC': 0.0,
         'description': 'МТС Mobile +7 981 333-44-55',
         'bonus': 0,
         'invest_bank': 0,
         'rounded_operation_sum': 150.0},
        {'operation_date': '07.03.2021 12:00:06',
         'payment_date': '07.03.2021',
         'card_number': 0,
         'status': 'OK',
         'sum_operation': -50.0,
         'currency_operation': 'RUB',
         'payment_sum': -50.0,
         'payment_currency': 'RUB',
         'cashback': 0.0,
         'category': 'Мобильная связь',
         'MCC': 0.0,
         'description': 'МТС Mobile +7 981 333-33-33',
         'bonus': 0,
         'invest_bank': 0,
         'rounded_operation_sum': 50.0
         },
        {'operation_date': '18.07.2020 21:05:23',
         'payment_date': '19.07.2020',
         'card_number': 0,
         'status': 'OK',
         'sum_operation': -50.0,

         'currency_operation': 'RUB',
         'payment_sum': -50.0,
         'payment_currency': 'RUB',
         'cashback': 0.0,
         'category': 'Мобильная связь',
         'MCC': 0.0,
         'description': 'МТС Mobile +7 921 999-99-99',
         'bonus': 0,
         'invest_bank': 0,
         'rounded_operation_sum': 50.0
         },

    ]


operations_dict = {
    "Дата операции": {
        0: Timestamp("2021-12-31 16:44:00"),
        1: Timestamp("2021-12-31 16:42:04"),
        2: Timestamp("2021-12-31 16:39:04"),
        3: Timestamp("2021-12-31 15:44:39"),
        4: Timestamp("2021-12-31 01:23:42"),
    },
    "Дата платежа": {
        0: Timestamp("2021-12-31 00:00:00"),
        1: Timestamp("2021-12-31 00:00:00"),
        2: Timestamp("2021-12-31 00:00:00"),
        3: Timestamp("2021-12-31 00:00:00"),
        4: Timestamp("2021-12-31 00:00:00"),
    },
    "Номер карты": {0: "*7197", 1: "*7197", 2: "*7197", 3: "*7197", 4: "*5091"},
    "Статус": {0: "OK", 1: "OK", 2: "OK", 3: "OK", 4: "OK"},
    "Сумма операции": {0: -160.89, 1: -64.0, 2: -118.12, 3: -78.05, 4: -564.0},
    "Валюта операции": {0: "RUB", 1: "RUB", 2: "RUB", 3: "RUB", 4: "RUB"},
    "Сумма платежа": {0: -160.89, 1: -64.0, 2: -118.12, 3: -78.05, 4: -564.0},
    "Валюта платежа": {0: "RUB", 1: "RUB", 2: "RUB", 3: "RUB", 4: "RUB"},
    "Кэшбэк": {0: None, 1: None, 2: None, 3: None, 4: None},
    "Категория": {
        0: "Супермаркеты",
        1: "Супермаркеты",
        2: "Супермаркеты",
        3: "Супермаркеты",
        4: "Различные товары",
    },
    "MCC": {0: 5411.0, 1: 5411.0, 2: 5411.0, 3: 5411.0, 4: 5399.0},
    "Описание": {0: "Колхоз", 1: "Колхоз", 2: "Магнит", 3: "Колхоз", 4: "Ozon.ru"},
    "Бонусы (включая кэшбэк)": {0: 3, 1: 1, 2: 2, 3: 1, 4: 5},
    "Округление на инвесткопилку": {0: 0, 1: 0, 2: 0, 3: 0, 4: 0},
    "Сумма операции с округлением": {0: 160.89, 1: 64.0, 2: 118.12, 3: 78.05, 4: 564.0},
}


@pytest.fixture
def input_dataframe():
    return pd.DataFrame(operations_dict)
