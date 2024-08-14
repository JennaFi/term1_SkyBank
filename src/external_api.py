import datetime
import json
import os
from typing import Any

import requests
import logging
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
api_key_stock = os.getenv("API_KEY_STOCK")
symbols = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'AMZN']

logger = logging.getLogger(__name__)

log_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "external_api.log")

logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_exchange_rates(api_key: any) -> Any:
    """Function fetches data from external api and writes it to json"""

    exchange_rates = {}

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/RUB"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if data["result"] == "success":
            rates = data.get('conversion_rates', {})
            rub_to_usd = round(1 / rates.get('USD'), 2)
            rub_to_eur = round(1 / rates.get('EUR'), 2)
            exchange_rates["USD"] = rub_to_usd
            exchange_rates["EUR"] = rub_to_eur

        else:
            raise Exception("API request failed with message: " + data["error-type"])

    except requests.exceptions.RequestException as e:

        print(f"HTTP request failed: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return exchange_rates


def get_stock_prices(api_key_stock, symbols):
    """Function fetches stock market prices"""

    base_url = f"https://financialmodelingprep.com/api/v3/quote/"

    stock_prices = {}

    for symbol in symbols:
        url = f"{base_url}{symbol}?apikey={api_key_stock}"
        response = requests.get(url)
        data = response.json()

        if data:
            stock_prices[symbol] = data[0].get('price')
        else:
            stock_prices[symbol] = None

    return stock_prices


try:
    exchange_rates = get_exchange_rates(api_key)
    stock_prices = get_stock_prices(api_key_stock, symbols)

    logger.info(f'{exchange_rates}, {stock_prices}')

except Exception as e:
    print(e)


print(get_exchange_rates(api_key), get_stock_prices(api_key_stock, symbols))

