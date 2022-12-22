import unittest
import csv_builder
from os import getcwd, path, remove

class TestProductDataQuery(unittest.TestCase):
    _console = "test_console"
    _base_path = getcwd() + "/data"
    
    def setUp(self):
        self._product_data = [
            {
                "id":1234,
                "consoleUri": "test_console",
                "productName": "test"
            },
            {
                "id":4321,
                "consoleUri": "test_console",
                "productName": "another test"
            }
        ]

        self._csv_builder = csv_builder.CsvBuilder(
            self._product_data,
            self._console
        )


    
    def test_build_full_path(self):
        print("\nStart sting set_full_path")

        self._csv_builder.build_full_path()

        self.assertEqual(
            self._csv_builder.get_full_path(),
            f"{self._base_path}/{self._console}.csv"
        )

    def test_write_product_data_to_csv(self):
        print("\nStart write_product_data_to_csv")

        self._csv_builder.write_product_data_to_csv()

        file_exists = path.isfile(self._csv_builder.get_full_path())

        self.assertTrue(file_exists)

        remove(f"{self._base_path}/{self._console}.csv")

