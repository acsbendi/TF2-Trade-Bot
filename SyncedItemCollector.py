from typing import List

from requests import get

from Item import Item
from ItemCollector import ItemCollector


class SyncedItemCollector(ItemCollector):

    def __init__(self):
        super().__init__()

    def _get_new_response(self):
        self._response = get(ItemCollector.STEAM_MARKET_SEARCH_URL, self._parameters)

    def _get_all_items(self):
        while self._total_item_count is None or self._parameters["start"] < self._total_item_count:
            print("start index = " + str(self._parameters["start"]))
            self._get_successful_response()
            if self._total_item_count is None:
                self._set_total_item_count()

            self._parameters["start"] += SyncedItemCollector.PAGESIZE

    def _get_successful_response(self):
        status_code = 0
        while status_code != 200:
            self._get_new_response()
            status_code = self._response.status_code
            print("trying....")
            print(str(self._response))

    def _set_total_item_count(self):
        self._total_item_count = self._response.json()["total_count"]
        print("total item count set: " + str(self._total_item_count))

    def _fill_item_list_from_hash_name(self):
        for item in self._response.json()["results"]:
            self._items.append(Item(item["hash_name"]))


