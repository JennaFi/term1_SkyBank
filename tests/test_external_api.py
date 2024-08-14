import os
from unittest.mock import patch, Mock

from src.external_api import get_exchange_rates, get_stock_prices

api_key = os.getenv("API_KEY")
api_key_stock = os.getenv("API_KEY_STOCK")


@patch("requests.get")
def test_get_exchange_rates(mock_get):
    mock_get.return_value.json.return_value = {
        "result": "success",
        "documentation": "https://www.exchangerate-api.com/docs",
        "terms_of_use": "https://www.exchangerate-api.com/terms",
        "time_last_update_unix": 1723248001,
        "time_last_update_utc": "Sat, 10 Aug 2024 00:00:01 +0000",
        "time_next_update_unix": 1723334401,
        "time_next_update_utc": "Sun, 11 Aug 2024 00:00:01 +0000",
        "base_code": "RUB",
        "conversion_rates": {
            "RUB": 1,
            "AED": 0.04199,
            "AFN": 0.8243,
            "ALL": 1.0663,
            "AMD": 4.5475,
            "ANG": 0.02047,
            "AOA": 10.4351,
            "ARS": 10.7438,
            "AUD": 0.01738,
            "AWG": 0.02047,
            "AZN": 0.01978,
            "BAM": 0.02047,
            "BBD": 0.02287,
            "BDT": 1.3555,
            "BGN": 0.02047,
            "BHD": 0.004299,
            "BIF": 33.6181,
            "BMD": 0.01143,
            "BND": 0.01513,
            "BOB": 0.08045,
            "BRL": 0.0633,
            "BSD": 0.01143,
            "BTN": 0.9591,
            "BWP": 0.1571,
            "BYN": 0.03713,
            "BZD": 0.02287,
            "CAD": 0.0157,
            "CDF": 33.2535,
            "CHF": 0.009882,
            "CLP": 10.9644,
            "CNY": 0.08269,
            "COP": 48.127,
            "CRC": 6.1456,
            "CUP": 0.2744,
            "CVE": 1.1539,
            "CZK": 0.2667,
            "DJF": 2.032,
            "DKK": 0.07829,
            "DOP": 0.6927,
            "DZD": 1.5672,
            "EGP": 0.5685,
            "ERN": 0.1715,
            "ETB": 1.1553,
            "EUR": 0.01047,
            "FJD": 0.02616,
            "FKP": 0.008962,
            "FOK": 0.07829,
            "GBP": 0.008964,
            "GEL": 0.03161,

            "USD": 0.01144,

        }
    }

    assert get_exchange_rates(api_key) == {'EUR': 95.51, 'USD': 87.41}

    mock_get.assert_called_once_with(
        f"https://v6.exchangerate-api.com/v6/{api_key}/latest/RUB")


@patch("requests.get")
def test_get_stock_prices(mock_get):
    mock_get.return_value.json.return_value = [
        {
            "symbol": "AAPL",
            "name": "Apple Inc.",
            "price": 216.24,
            "changesPercentage": 1.3736,
            "change": 2.93,
            "dayLow": 211.98,
            "dayHigh": 216.78,
            "yearHigh": 237.23,
            "yearLow": 164.08,
            "marketCap": 3287734584000,
            "priceAvg50": 214.237,
            "priceAvg200": 190.21304,
            "exchange": "NASDAQ",
            "volume": 39697781,
            "avgVolume": 66472222,
            "open": 212.1,
            "previousClose": 213.31,
            "eps": 6.57,
            "pe": 32.91,
            "earningsAnnouncement": "2024-10-31T10:59:00.000+0000",
            "sharesOutstanding": 15204100000,
            "timestamp": 1723233601
        },
    ]

    symbols = ['AAPL']

    assert get_stock_prices(api_key_stock, symbols) == {'AAPL': 216.24}

    mock_get.assert_called_once_with(f"https://financialmodelingprep.com/api/v3/quote/AAPL?apikey={api_key_stock}")


@patch("requests.get")
def test_get_stock_prices_empty_data(mock_get):
    mock_get.return_value.json.return_value = []
    symbols = ['AAPL']
    assert get_stock_prices(api_key_stock, symbols) == {'AAPL': None}


@patch("requests.get")
def test_get_stock_prices_error_response(mock_get):
    mock_get.return_value.json.return_value = {}
    symbols = ['AAPL']
    assert get_stock_prices(api_key_stock, symbols) == {'AAPL': None}



