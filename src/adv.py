from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", Item("Small Torch", "Used for exploring.")),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Item("Dirty Map", "Map that is too dirty to see properly.")),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Item("Small Stick", "Weak weapon used to fight enemies.")),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Item("Small Rock", "Small pebble that the passage is full of.")),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Item("Empty Bag of coins", "Cloth bags used for carrying coins that have nothing inside of them")),
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

user = input("\nWhat is your name?\n")
player = Player(user, room['outside'])
print(
    f"\nWelcome {player.name}!\n{player.current_room}\n")

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

items = []

while True:
    press = input(
        "\nNorth [n] South [s] East [e] West [w] Quit [q]\nRoom Update [u] Inventory [i] Take Item [take {item name}] Drop Item [drop {item name}]\n")

    if(press == "q"):
        print("Quitting Game...")
        break
    elif(press == "n"):
        if(player.current_room.n_to == None):
            print("\nThat direction does not exist\n")
        else:
            player.current_room = player.current_room.n_to
            print(f"\n{player.current_room}\n")
    elif(press == "s"):
        if(player.current_room.s_to == None):
            print("\nThat direction does not exist\n")
        else:
            player.current_room = player.current_room.s_to
            print(f"\n{player.current_room}\n")
    elif(press == "e"):
        if(player.current_room.e_to == None):
            print("\nThat direction does not exist\n")
        else:
            player.current_room = player.current_room.e_to
            print(f"\n{player.current_room}\n")
    elif(press == "w"):
        if(player.current_room.w_to == None):
            print("\nThat direction does not exist\n")
        else:
            player.current_room = player.current_room.w_to
            print(f"\n{player.current_room}\n")
    elif(press == "i"):
        if(len(items) == 0):
            print("\nYou have no Items\n")
        else:
            print(items)
    elif(press == "u"):
        print(f"\n{player.current_room}\n")
    elif(press[0] == "take"):
        if(len(player.current_room.item) > 0):
            player.pickup(player.current_room.item)
        else:
            print("Empty Room")
            player.current_room.item = None
    # elif(press.split(" ")[0] == f"drop {player.current_room.item.name}"):
    #     print("items", items)
    #     items.remove(player.current_room.item.name)
    #     player.current_room.item.append(player.current_room.item.name)
    else:
        print("\nWrong Input!\n")
