from abc import ABC, abstractmethod
from typing import List

from requests import get

from Item import Item


class ItemCollector(ABC):

    STEAM_MARKET_SEARCH_URL = 'https://steamcommunity.com/market/search/render/'
    PAGESIZE = 100

    def __init__(self):
        self._parameters = {
            "appid": 440,
            "norender": True,
            "count": ItemCollector.PAGESIZE,
            "start": 0
        }
        self._total_item_count = None
        self._response = None
        self._items = List[Item]

    def _get_successful_response(self, parameters: dict):
        status_code = 0
        while status_code != 200:
            self._get_new_response(parameters)
            status_code = self._response.status_code
            print("trying....")
            print(str(self._response))

    def fill_item_list(self, item_list: List[Item]):
        self._get_all_items()
        item_list.extend(self._items)

    def _set_total_item_count(self):
        self._total_item_count = self._response.json()["total_count"]
        print("total item count set: " + str(self._total_item_count))

    def _get_new_response(self, parameters: dict):
        print("get called with parameters", parameters)
        self._response = get(ItemCollector.STEAM_MARKET_SEARCH_URL, parameters)

    @abstractmethod
    def _get_all_items(self):
        raise NotImplementedError