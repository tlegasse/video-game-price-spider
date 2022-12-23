import requests
from typing import List, Dict
import time

class ProductDataQuery:
    _base_url = "https://www.pricecharting.com/console"
    _cursor = 0
    _return_format = "json"
    _product_data = []
    _console = ""

    def __init__(self):
        self._endpoint = self.get_endpoint()
        self._params = self.get_params()

    def set_console(self,console:str):
        self._console = console

    def set_cursor(self, cursor):
        self._cursor = cursor

    def get_console(self):
        return self._console

    def get_base_url(self):
        return self._base_url

    def get_cursor(self):
        return self._cursor

    def get_product_data(self):
        return self._product_data

    def get_params(self):
        return {
            "cursor": self._cursor,
            "format": self._return_format
        }

    def append_product_data(self, products: List[Dict]):
        self._product_data.extend(products)

    def call_data(self):
        response = requests.request(
            "GET",
            self.get_endpoint(),
            params = self.get_params()
        )

        if response.status_code == 404:
            print(f"Couldn't query for {self.get_console()}")
            return

        response_json = response.json()

        self.append_product_data(response_json['products'])

        if 'cursor' not in response_json:
            return

        self.set_cursor(int(response_json['cursor']))

        if self._cursor:
            self.call_data()

    def get_endpoint(self):
        return f"{self._base_url}/{self._console}"
