from Item import Item
from ItemCollector import ItemCollector


class SyncedItemCollector(ItemCollector):

    def __init__(self):
        super().__init__()

    def _get_all_items(self):
        while self._total_item_count is None or self._parameters["start"] < self._total_item_count:
            print("start index = " + str(self._parameters["start"]))
            self._get_successful_response(self._parameters)
            if self._total_item_count is None:
                self._set_total_item_count()

            self._parameters["start"] += ItemCollector.PAGESIZE

    def _fill_item_list_from_hash_name(self):
        for item in self._response.json()["results"]:
            self._items.append(Item(item["hash_name"]))


