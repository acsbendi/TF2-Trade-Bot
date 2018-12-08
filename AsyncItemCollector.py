import asyncio
import concurrent
from math import ceil

from ItemCollector import ItemCollector


class AsyncItemCollector(ItemCollector):

    def __init__(self):
        super().__init__()
        self._loop = asyncio.get_event_loop()

    def _get_all_items(self):
        self._set_total_item_count_from_first_response()

        self._loop.run_until_complete(self._async_get_all_items())

    def _set_total_item_count_from_first_response(self):
        self._get_successful_response_and_increase_start()
        self._set_total_item_count()

    def _get_successful_response_and_increase_start(self):
        self._get_successful_response(dict(self._parameters))
        self._parameters["start"] += ItemCollector.PAGESIZE

    async def _async_get_all_items(self):
        worker_count = ceil(self._total_item_count / ItemCollector.PAGESIZE)
        with concurrent.futures.ThreadPoolExecutor(max_workers=worker_count) as executor:
            futures = []
            while self._parameters["start"] < self._total_item_count:
                futures.append(
                    self._loop.run_in_executor(
                        None,
                        self._get_successful_response_and_increase_start
                    )
                )
                self._parameters["start"] += ItemCollector.PAGESIZE

            for response in await asyncio.gather(*futures):
                pass
