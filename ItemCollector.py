from abc import ABC, abstractmethod
from typing import List

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

    def fill_item_list(self, item_list: List[Item]):
        self._get_all_items()
        item_list.extend(self._items)

    @abstractmethod
    def _get_all_items(self):
        raise NotImplementedError