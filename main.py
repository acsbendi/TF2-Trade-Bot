from Item import Item
from ItemContainer import ItemContainer
from SyncedItemCollector import SyncedItemCollector

items = [
    Item("Vintage Warrior's Spirit"),
    Item("Strange Jag"),
    Item("Genuine Sun-on-a-Stick"),
    Item("Strange Rat Stompers"),
    Item("Strange Southern Hospitality"),
    Item("Scot Bonnet"),
    Item("Description Tag"),
    Item("Strange Clubsy The Seal"),
    Item("Gift Wrap"),
    Item("Mann Co. Supply Crate Key"),
    Item("Strange SMG"),
    Item("Vintage Sun-on-a-Stick"),
    Item("Haunted Dark Helm"),
    Item("Strange Lurker's Leathers"),
    Item("Strange Rust Botkiller Stickybomb Launcher Mk.I"),
    Item("Strange Axtinguisher"),
    Item("Genuine Tough Guy's Toque")
]

synced_item_collector = SyncedItemCollector()

synced_item_collector.fill_item_list(items)

item_container = ItemContainer()

item_container.deserialize("items.txt")

for item in items:
    item_container.add_item(item)

#item_container.get_steam_market_prices_for_all_items()

item_container.print_all()

item_container.serialize("items.txt")