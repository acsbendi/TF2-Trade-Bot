from jsonpickle import decode

from requests import get

from Item import Item
from Sum import Sum


class ItemContainer:

    def __init__(self):
        self._items = []

    def add_item(self, new_item: Item):
        if new_item not in self._items:
            print("adding new item " + str(new_item))
            self._items.append(new_item)

    def serialize(self, file_name: str):
        with open(file_name, "w+") as outfile:
            for item in self._items:
                outfile.write(str(item) + "\n")

    def deserialize(self, file_name: str):
        try:
            with open(file_name, "r") as infile:
                for line in infile:
                    print("read : " + line)
                    item = decode(line)
                    self._items.append(item)
        except FileNotFoundError:
            print("Could not deserialized")

    def print_all(self):
        for item in self._items:
            print(str(item))

    def get_steam_market_prices_for_all_items(self):
        url_prefix = "https://steamcommunity.com/market/priceoverview/?appid=440&currency=3&market_hash_name="
        for item in self._items:
            response = get(url_prefix + item.get_url_ending())
            print("response received : " + str(response))
            lowest_price_on_steam_market = response.json()["lowest_price"]
            item.update_steam_market_price(Sum(lowest_price_on_steam_market))