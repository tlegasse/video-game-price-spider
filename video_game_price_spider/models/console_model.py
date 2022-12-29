from peewee import CharField, IntegerField
from video_game_price_spider.models.base_model import Base

class Console(Base):
    id: IntegerField = IntegerField(primary_key=True, unique=True)
    name: CharField = CharField()
    slug: CharField = CharField()
