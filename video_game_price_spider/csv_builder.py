import os
import pandas as pd


class CsvBuilder:
    _base_path: str = "./price_entries"
    _full_path: str
    _console: str
    _product_data: list = []

    def __init__(self, product_data: list, console: str)-> None:
        self.set_product_data(product_data)
        self.set_console(console)
        self.build_full_path()

        if not os.path.isdir(self._base_path):
            os.makedirs(self._base_path)

    def set_product_data(self, product_data: list)-> None:
        self._product_data: list = product_data

    def set_console(self, console)-> None:
        self._console: str = console

    def get_full_path(self)-> str:
        return self._full_path

    def build_full_path(self)-> None:
        self._full_path: str = f"{self._base_path}/{self._console}.csv"

    def write_product_data_to_csv(self)-> None:
        prepared_data:dict = {}

        for item in self._product_data:
            for column in item.keys():
                if column not in prepared_data:
                    prepared_data[column] = []

                prepared_data[column].append(item[column])

        data_frame:pd.DataFrame = pd.DataFrame(data=prepared_data)
        data_frame.to_csv(self._full_path)
