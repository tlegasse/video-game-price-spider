import requests

class ProductDataQuery:
    _base_url:str = "https://www.pricecharting.com/console"
    _cursor: int = 0
    _return_format:str = "json"
    _product_data:list = []
    _console:str = ""

    def __init__(self) -> None :
        self._endpoint:str = self.get_endpoint()
        self._params:dict = self.get_params()

    def set_console_string(self,console:str)-> None:
        self._console: str = console

    def set_cursor(self, cursor)-> None:
        self._cursor: int = cursor

    def get_console(self)->str :
        return self._console

    def get_base_url(self)-> str:
        return self._base_url

    def get_cursor(self)-> int:
        return self._cursor

    def get_product_data(self)-> list:
        return self._product_data

    def get_params(self) -> dict:
        return {
            "cursor": self._cursor,
            "format": self._return_format
        }

    def append_product_data(self, products: list)-> None:
        self._product_data.extend(products)

    def call_data(self)-> None:
        response: requests.Response = requests.request(
            "GET",
            self.get_endpoint(),
            params = self.get_params()
        )

        if response.status_code == 404:
            print(f"Couldn't query for {self.get_console()}")
            return

        response_json:dict = response.json()

        self.append_product_data(response_json['products'])

        if 'cursor' not in response_json:
            return

        self.set_cursor(int(response_json['cursor']))

        if self._cursor:
            self.call_data()

    def get_endpoint(self)-> str:
        return f"{self._base_url}/{self._console}"
