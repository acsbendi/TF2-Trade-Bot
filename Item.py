from jsonpickle import encode

from Sum import Sum


class Item:

    def __init__(self, full_name : str):
        self._full_name = full_name
        self._steam_market_price = Sum("0E")
        self._backpack_price = Sum("0E")

    def update_backpack_price(self, new_price: Sum):
        self._backpack_price = new_price

    def update_steam_market_price(self, new_price: Sum):
        self._steam_market_price = new_price

    def get_url_ending(self):
        return self._full_name

    def __str__(self):
        return encode(self)

    def __eq__(self, other):
        if isinstance(other, Item):
            return self._full_name == other._full_name
        return False

