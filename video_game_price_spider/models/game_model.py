from peewee import CharField, IntegerField
from video_game_price_spider.models.base_model import Base

class Game(Base):
    id: IntegerField = IntegerField(primary_key=True, unique=True)
    name: CharField = CharField()
    console_uri: CharField = CharField()
    price_1: CharField = CharField()
    price_2: CharField = CharField()
    price_3: CharField = CharField()
    price_change: CharField = CharField()
    price_change_percentage: CharField = CharField()
    price_change_sign: CharField = CharField()
    product_name: CharField = CharField()
    product_uri: CharField = CharField()
