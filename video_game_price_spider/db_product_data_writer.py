from video_game_price_spider.product_data_writer import ProductDataWriter
from video_game_price_spider.models.game_model import Game

from peewee import SqliteDatabase

class DbProductDataWriter(ProductDataWriter):
    _product_data: list = []
    _console: str

    def __init__(self, product_data, console) -> None:
        self.set_console(console)
        self.set_product_data(product_data)
        self.init_database_if_not_exists()

    def write_product_data(self) -> None:
        for product in self._product_data:

            if product["price1"] != '':
                price1 = float(
                    product["price1"] \
                    .replace("$",'') \
                    .replace(',','')
                )
            else:
                price1 = 0.0

            if product["price2"] != '':
                price2 = float(
                    product["price2"] \
                    .replace("$",'') \
                    .replace(',','')
                )
            else:
                price2 = 0.0

            if product["price3"] != '':
                price3 = float(
                    product["price3"] \
                    .replace("$",'') \
                    .replace(',','')
                )
            else:
                price3 = 0.0

            game = Game.insert(
                id=product["id"],
                console_uri=product["consoleUri"],
                price_1=price1,
                price_2=price2,
                price_3=price3,
                price_change=product["priceChange"],
                price_change_percentage=product["priceChangePercentage"],
                price_change_sign=product["priceChangeSign"],
                product_name=product["productName"],
                product_uri=product["productUri"]
            ).on_conflict_replace().execute()

    def set_product_data(self, product_data) -> None:
        self._product_data = product_data

    def set_console(self, console)-> None:
        self._console: str = console

    def init_database_if_not_exists(self):
        db: SqliteDatabase = SqliteDatabase("games.db")

        db.create_tables([Game])


    
