from peewee import CharField, FloatField, IntegerField
from video_game_price_spider.models.base_model import Base

class Game(Base):
    id: IntegerField = IntegerField(primary_key=True, unique=True)
    console_uri: CharField = CharField()
    price_1: FloatField = FloatField()
    price_2: FloatField = FloatField()
    price_3: FloatField = FloatField()
    price_change: CharField = CharField()
    price_change_percentage: CharField = CharField()
    price_change_sign: CharField = CharField()
    product_name: CharField = CharField()
    product_uri: CharField = CharField()
