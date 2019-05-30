# Write a class to hold player information, e.g. what room they are in
# currently.
valid_directions = ["n", "s", "e", "w"]

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
    def move(self, direction):
        if direction in valid_directions:
            next_room = getattr(self.room, f"{direction}_to")
            if (next_room) is not None:
                self.room = next_room
            else:
                print("Cannot move in that direction!\n")
        else:
            print("Not a valid direction, try again!\n")
