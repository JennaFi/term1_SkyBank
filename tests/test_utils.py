from datetime import datetime
from unittest.mock import patch, mock_open

import pytest

from src.utils import get_greeting, get_operations_data_from_excel, get_cards_numbers, get_sum_expenses_by_card, \
    get_cashback_by_card, get_top_5_transactions, get_greeting, get_current_month_operations, get_user_settings


@patch("src.utils.datetime")
@pytest.mark.parametrize(
    "current_hour, expected_greeting",
    [
        (7, "Доброе утро!"),
        (14, "Добрый день!"),
        (20, "Добрый вечер!"),
        (4, "Доброй ночи!"),
    ],
)
def test_get_greeting(mock_datetime, current_hour, expected_greeting):
    mock_now = datetime(2021, 7, 25, current_hour, 0, 0)
    mock_datetime.datetime.now.return_value = mock_now
    result = get_greeting()
    assert result == expected_greeting


def test_get_operations_data_from_excel(file_path):

    assert get_operations_data_from_excel('../data/operations.xlsx')[0] == {
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
    }


def test_get_cards_numbers(operations):
    assert get_cards_numbers(operations) == ['*7197', '*5091']


def test_get_sum_expenses_by_card(operations, month_year):
    assert get_sum_expenses_by_card(operations, '31.12.2021') == [
        {'card_number': '*7197', 'all_payments': 160.89},
        {'card_number': '*5091', 'all_payments': 564.0},
        {'card_number': 0, 'all_payments': 800.0},
    ]


def test_get_cashback_by_card(operations, month_year):
    assert get_cashback_by_card(operations, '31.12.2021') == [
        {'card_number': '*7197', 'cashback': 4.21},
        {'card_number': '*5091', 'cashback': 5.64}
    ]


def test_get_top_5_transactions(operations, month_year):
    assert get_top_5_transactions(operations, '31.12.2021') == [
        {'transaction': 800.0, 'description': 'Константин Л.'},
        {'transaction': 564.0, 'description': 'Ozon.ru'},
        {'transaction': 160.89, 'description': 'Колхоз'},
        {'transaction': 118.12, 'description': 'Магнит'},
        {'transaction': 78.05, 'description': 'Колхоз'}

    ]


def test_get_current_month_operations(input_dataframe):
    assert input_dataframe.equals(get_current_month_operations(input_dataframe, "31.12.2021"))
