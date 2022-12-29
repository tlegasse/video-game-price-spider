from peewee import ForeignKeyField
from video_game_price_spider.models.game_model import Game
from video_game_price_spider.models.console_model import Console
from video_game_price_spider.models.base_model import Base

class GameConsoleRelationship(Base):
    from_console = ForeignKeyField(Console)
    to_game = ForeignKeyField(Game)
