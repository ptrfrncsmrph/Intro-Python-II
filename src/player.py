# Write a class to hold player information, e.g. what room they are in
# currently.

def lookup_item(str, items):
    """
    Takes a name and an iterable of items, and returns
    the item with a matching name, or None.
    """
    for item in items:
        if item.name == str:
            return item
        else:
            return None


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []
    def move(self, direction):
        next_room = getattr(self.room, f"{direction}_to")
        if (next_room) is not None:
            self.room = next_room
        else:
            print("Cannot move in that direction!\n")
    def show_items(self):
        if self.items.__len__() == 0:
            return "no items"
        else:
            return ", ".join(list(map(lambda it: it.name, self.items)))
    def do(self, cmd):
        if cmd in ("i", "inventory"):
            print(f"You've got: {self.show_items()}")
        else: 
            action, item_name = cmd.split(" ")
            if action in ("get", "take"):
                item = lookup_item(item_name, self.room.items)
                if item is not None:
                    self.room.items.remove(item)
                    self.items.append(item)
                    item.on_take()
                else:
                    print(f"Could not find item with name {item_name} in this room.\n")
            elif action == "drop":
                item = lookup_item(item_name, self.items)
                if item is not None:
                    self.items.remove(item)
                    self.room.items.append(item)
                    item.on_drop()
                else:
                    print(f"Could not find item with name {item_name} in your items.\n")
            else:
                print(f"Unrecognized action: {action}\n")
