import json
import os

import click

from video_game_price_spider.csv_product_data_writer import CsvProductDataWriter
from video_game_price_spider.db_product_data_writer import DbProductDataWriter
from video_game_price_spider.product_data_query import ProductDataQuery
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

    def update_by_console(console: str, method: str) -> None:
        console_data_query: ProductDataQuery = ProductDataQuery()
        console_data_query.set_console_string(console)

        print(f"Querying {console}")
        console_data_query.call_data()

        if method == "csv":
            console_csv_product_data_writer:CsvProductDataWriter = CsvProductDataWriter(console_data_query.get_product_data(),console)
            console_csv_product_data_writer.write_product_data()
        else:
            console_db_product_data_writer: DbProductDataWriter = DbProductDataWriter(console_data_query.get_product_data(),console)
            console_db_product_data_writer.write_product_data()

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
                consoles_found.append(found_console)

        return consoles_found


    consoles_to_sync: list = []

    consoles_to_sync.extend(get_consoles_from_brands(ctx, brands))
    consoles_to_sync.extend(get_matched_consoles(ctx, consoles))

    for console in consoles_to_sync:
        update_by_console(console, method)


@cli.command()
@click.option('--title', '-t')
@click.pass_obj
def search(ctx, title):
    games = Game.select().where(Game.product_name.contains(title))

    for game in games:
        print(game.product_name)
        # print(game["productName"])
