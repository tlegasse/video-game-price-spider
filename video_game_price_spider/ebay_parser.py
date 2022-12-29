from bs4 import BeautifulSoup
import requests
import urllib.parse
from terminaltables import AsciiTable

class EbayParser():
    _found_games: list[dict] = []
    _notable_listings: list[dict] = []
    _base_search_str: str = "https://www.ebay.com/sch/i.html"


    def __init__(self, found_games):
        self._found_games = found_games

    def get_search_strings(self, game, condition):
        game_title = game.product_name + " "

        if condition != "loose":
            game_title = game_title + condition

        console_title = game.console_uri.replace('-', ' ')

        game_title = game_title + console_title

        game_title = urllib.parse.quote(game_title)


        return game_title

    def find_listings(self) -> None:
        params_list = []
        for game in self._found_games:

            prices = {
                "loose": game.price_1,
                "cib": game.price_3,
                "sealed": game.price_2
            }

            for condition in prices:
                title_encoded = self.get_search_strings(game, condition)

                params_list.append(self.build_query(title_encoded, prices[condition]))

        self.make_requests(params_list)

    def make_requests(self, params_list):

        table_data = [
            ["title", "price", "Expected Price", "url"]
        ]

        for params in params_list:
            response = requests.get(
                url=self._base_search_str,
                params=params
            )

            content = response.content

            parsed_content = BeautifulSoup(content, 'html.parser')

            listings = parsed_content.findAll("div", {"class": 's-item__wrapper'})

            for listing in listings:
                table_data.append([
                    listing.find("span", {"role": "heading"}).getText(),
                    "$" + str(params["_udhi"]),
                    listing.find("span", {"class": "s-item__price"}).getText(),
                    listing.find("a", {"class": "s-item__link"}, href=True)['href']
                ])

        table = AsciiTable(table_data)
        print(table.table)



    def build_query(self, title_encoded, price_high):
        params = {
            "_nkw": title_encoded, # Encoded search keyword
            "_sacat": 139973, # Category
            # "_udlo": price_low, # Price low
            "_udhi": price_high, # Price high
            "LH_BIN": 1, # Buy it now
            "LH_ItemCondition": 4000, # Item condition
            "rd": "nc"
        }

        return params
