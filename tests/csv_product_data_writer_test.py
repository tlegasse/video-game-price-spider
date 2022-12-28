from os import path, remove
import unittest

from video_game_price_spider.csv_product_data_writer import CsvProductDataWriter
from video_game_price_spider.product_data_writer import ProductDataWriter


class TestProductDataQuery(unittest.TestCase):
    _console: str = "test_console"
    _base_path: str = "./price_entries"

    def setUp(self) -> None :
        self._product_data: list[dict[str]] = [
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

        self._csv_product_data_writer: CsvProductDataWriter = CsvProductDataWriter(
            self._product_data,
            self._console
        )

    def test_build_full_path(self) -> None:
        print("\nStart build_full_path")

        self._csv_product_data_writer.build_full_path()

        self.assertEqual(
            self._csv_product_data_writer.get_full_path(),
            f"{self._base_path}/{self._console}.csv"
        )

    def test_write_product_data(self) -> None :
        print("\nStart write_product_data")

        self._csv_product_data_writer.write_product_data()

        file_exists = path.isfile(self._csv_product_data_writer.get_full_path())

        self.assertTrue(file_exists)

        remove(f"{self._base_path}/{self._console}.csv")

