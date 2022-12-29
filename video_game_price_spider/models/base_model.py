from peewee import SqliteDatabase, Model

db: SqliteDatabase = SqliteDatabase("games.db")

class Base(Model):
    class Meta:
        database: SqliteDatabase = db
