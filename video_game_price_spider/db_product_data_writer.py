from video_game_price_spider.product_data_writer import ProductDataWriter
import sqlite3

class DbProductDataWriter(ProductDataWriter):
    _product_data: list = []
    _console: str

    def __init__(self) -> None:
        self.set_console(console)

    def write_product_data(self) -> None:
        pass

    def set_console(self, console)-> None:
        self._console: str = console


    
