import os
from typing import List, Dict
import pandas as pd

class CsvBuilder:
    _base_path = os.getcwd() + "/data"
    _full_path: str
    _console: str
    _product_data: List[Dict] = []
    _columns_to_write: List[str] = [
        "consoleUri",
        "hasProduct",
        "id",
        "price1",
        "price2",
        "price3",
        "priceChange",
        "priceChangePercentage",
        "priceChangeSign",
        "printRun",
        "productName",
        "productUri"
    ]

    def __init__(self, product_data: List[Dict], console: str):
        self.set_product_data(product_data)
        self.set_console(console)
        self.build_full_path()

    def set_product_data(self, product_data: List[Dict]):
        self._product_data = product_data

    def set_console(self, console):
        self._console = console

    def get_full_path(self):
        return self._full_path
        
    def build_full_path(self):
        self._full_path = f"{self._base_path}/{self._console}.csv"

    def write_product_data_to_csv(self):

        prepared_data = {}

        for item in self._product_data:
            for column in item.keys():
                if column not in prepared_data:
                    prepared_data[column] = []

                prepared_data[column].append(item[column])
                

        df = pd.DataFrame(data=prepared_data)
        df.to_csv(self._full_path)


