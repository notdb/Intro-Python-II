from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}



# Link rooms together
linked_rooms = {
room['outside'].n_to : room['foyer'],
room['foyer'].s_to : room['outside'],
room['foyer'].n_to : room['overlook'],
room['foyer'].e_to : room['narrow'],
room['overlook'].s_to : room['foyer'],
room['narrow'].w_to : room['foyer'],
room['narrow'].n_to : room['treasure'],
room['treasure'].s_to : room['narrow'],
}

print(room['overlook'].n_to in linked_rooms)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

player = Player("The Player", room['outside'])


quit = False

while not quit:
   
    print(f"You are in the {player.current_room}\n \n")

    user_input = input("Enter a direction:\n\n(N)orth\n(S)outh\n(E)ast\n(W)est\n\n(Q)uit\n\nWhere should we go? \n ")

    if user_input == '':
        continue
    
    user_input = user_input.lower().strip()[0]

    if user_input == 'q':
        quit = True

    if user_input == 'n':
        try_again_room = player.current_room
        player.current_room = player.current_room.n_to
        if linked_rooms.get(player.current_room) is None:
            print("\nError room not found\nTry Again")
            player.current_room = try_again_room
        else:
            for k, v in linked_rooms.items():
                if k == player.current_room:
                    player.current_room = v
                    break


    if user_input == 's':
        try_again_room = player.current_room
        player.current_room = player.current_room.s_to
        if linked_rooms.get(player.current_room) is None:
            print("Error room not found")
            player.current_room = try_again_room
        for k, v in linked_rooms.items():
            if k == player.current_room:
                player.current_room = v
                break


    if user_input == 'e':
        try_again_room = player.current_room
        player.current_room = player.current_room.e_to
        if linked_rooms.get(player.current_room) is None:
            print("Error room not found")
            player.current_room = try_again_room
        for k, v in linked_rooms.items():
            if k == player.current_room:
                player.current_room = v
                break

    if user_input == 'w':
        try_again_room = player.current_room
        player.current_room = player.current_room.w_to
        if linked_rooms.get(player.current_room) is None:
            print("Error room not found")
            player.current_room = try_again_room
        for k, v in linked_rooms.items():
            if k == player.current_room:
                player.current_room = v
                break
  
