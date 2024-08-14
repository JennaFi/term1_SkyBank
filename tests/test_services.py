

from src.services import simple_search, search_by_phone_number


def test_simple_search(operations):
    search_str = "Переводы"
    expected_result = [

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
        },
    ]

    assert simple_search(operations, search_str) == expected_result


def test_search_by_phone_number(operations_phone):
    assert search_by_phone_number(operations_phone) == operations_phone
