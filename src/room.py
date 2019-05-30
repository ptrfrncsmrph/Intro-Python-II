# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap

valid_directions = ("n", "s", "e", "w")
horizontal_line = "**********************"
def to_upper(str):
    return str.upper()

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def show_items(self):
        if self.items.__len__() == 0:
            return "no items"
        else:
            return ", ".join(list(map(lambda it: it.name, self.items)))
    def show_directions(self):
        possible_directions = filter(lambda d: getattr(self, f"{d}_to") is not None, valid_directions)
        return ", ".join(list(map(to_upper, possible_directions)))
    def __str__(self):
        return "\n\n".join(
            [ self.name
            , horizontal_line
            , textwrap.fill(self.description)
            , "Room contents: " + self.show_items()
            , "Possible directions: " + self.show_directions()
            ])