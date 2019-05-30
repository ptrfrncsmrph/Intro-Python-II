# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
    def change_room(self, new_room):
        self.room = new_room
    def get_room(self):
        return self.room