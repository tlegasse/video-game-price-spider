import json
import os
import click
from peewee import SqliteDatabase

from video_game_price_spider.models.console_model import Console
from video_game_price_spider.models.game_console_relationship_model import GameConsoleRelationship
from video_game_price_spider.models.game_model import Game

def load_console_json() -> dict :
    path: str = os.path.join(os.getcwd(), 'data', 'console_data.json')
    with open(path) as f:
        data: dict = json.load(f)
        return data


@click.group()
@click.pass_context
def cli(ctx) -> None :
    ctx.obj = load_console_json()["available_console_strings"]


@cli.command()
@click.pass_obj
def list_consoles(ctx) -> None :
    """
    Lists known console data by manufacturer
    """

    for brand in ctx:
        click.echo(brand)

        for console in ctx[brand]:
            click.echo("  " + console)

        click.echo()

@cli.command()
@click.option('--brands', '-b', multiple=True, help="Brands to sync from")
@click.option('--consoles', '-c', multiple=True, help="Consoles to sync from")
@click.option('--method', '-m', multiple=False, default="csv", type=click.Choice(["csv","db"]), help="Method of delivery, either CSV or SqLite")
@click.pass_obj
def sync_console_data(ctx, method: str, brands: list[str], consoles: list[str]) -> None :
    """
    Syncs data from price chart by console or brand
    """

    def init_database_if_not_exists():
        db: SqliteDatabase = SqliteDatabase("games.db")

        db.create_tables([Game, Console, GameConsoleRelationship])


    def get_consoles_from_brands(ctx, brands: list[str]) -> list[str] :
        consoles_found: list = []
        
        for brand in brands:
            if brand in ctx:
                consoles_found.extend(ctx[brand])
            else:
                click.echo("Brand not found: " + brand)

        return consoles_found


    def get_matched_consoles(ctx, consoles: list[str]) -> list[str]:
        consoles_found: list = []

        for console in consoles:
            found_console: Literal[False] | str = False

            for brand in ctx:
                if console in ctx[brand]:
                    found_console = console

            if not found_console:
                click.echo("Console not found: " + console)
            else:
                consoles_found.append(consoles_to_sync)

        return consoles_found


    consoles_to_sync: list = []

    consoles_to_sync.extend(get_consoles_from_brands(ctx, brands))

    consoles_to_sync.extend(get_matched_consoles(ctx, consoles))


    init_database_if_not_exists()
    
    game: Game = Game.create(
        id=1,
        name="game name",
        console_uri="console_uri",
        price_1="12.10",
        price_2="12.10",
        price_3="12.10",
        price_change="12.10",
        price_change_percentage="12.10",
        price_change_sign="+",
        product_name="Some Game",
        product_uri="some-game",
    )

    console: Console = Console.create(
        id=1,
        slug="some-console",
        name="Some console name"
    )


# def update_by_console(console: str):
    # console_data_query = ProductDataQuery()
    # console_data_query.set_console_string(console)

    # print(f"Querying {console}")
    # console_data_query.call_data()

    # console_csv_product_data_writer = CsvProductDataWriter(console_data_query.get_product_data(),console)
    # console_csv_product_data_writer.write_product_data()
