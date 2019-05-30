from room import (Room, valid_directions)

from item import Item

rock = Item("rock", "A large rock")
coins = Item("coins", "Shiny coins")
sword = Item("sword", "A sharp sword")
lantern = Item("lantern", "A bright lantern")

# Declare all the rooms

room = {
    'outside':  Room( "Outside Cave Entrance"
                    , "North of you, the cave mount beckons"
                    , [rock]),

    'foyer':    Room( "Foyer"
                    , """Dim light filters in from the south. Dusty passages run north and east."""
                    , [sword]),

    'overlook': Room( "Grand Overlook"
                    , """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""
                    , []),

    'narrow':   Room( "Narrow Passage"
                    , """The narrow passage bends here from west to north. The smell of gold permeates the air."""
                    , [lantern]),

    'treasure': Room( "Treasure Chamber"
                    , """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""
                    , [coins]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

from player import Player
player = Player("Pete", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
valid_actions = ("drop", "take", "get")

def is_direction(str):
    """
    Takes a string and returns true if it is a valid direction
    """
    return str in valid_directions

def is_command(str):
    """
    Takes a string and returns true if it is a valid command
    ('get' or 'take' followed by an item name). It does not
    validate the item name.
    """
    split_str = str.split(" ")
    return split_str.__len__() == 2 and split_str[0] in valid_actions

print(player.room)
current_room = player.room

while True:
    if current_room != player.room:
        print(player.room)
        current_room = player.room
    current_room = player.room
    cmd = input("\nWhat do you want to do?\n> ")
    if cmd == "q":
        break
    elif is_direction(cmd):
        player.move(cmd)
    elif is_command(cmd):
        player.do(cmd)
    else:
        print("\nDid not recognize that command, please try again!")
