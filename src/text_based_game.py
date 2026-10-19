"""Project Two starter for the student's text-based adventure game."""

# Author: Abel Antonio Cardenas Jaimes


def show_instructions():
    """Display the game objective and available commands."""
     print("Welcome to Mystical Elemental Island!")
    print("Collect all 6 items before facing Zeus.")
    print("Move commands: go north, go south, go east, go west")
    print("Collect items: get <item name>")
    print("Avoid the Pit of Lions. It is a trap!")
    print("----------------------------------------")



def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("----------------------------------------")
    print("You are in", current_room)
    print("Inventory:", inventory)

    if 'item' in rooms[current_room]:
        print("You see", rooms[current_room]['item'])


def main():
    """Run the main gameplay loop."""
    # Rooms, directions, and items from Project One.
    # TODO: Set the player's starting room.
     rooms = {
        'Ancestral Village': {
            'west': 'Sacred River',
            'east': 'Altar of Olympus'
        },
        'Sacred River': {
            'north': 'Temple of Fire',
            'east': 'Ancestral Village',
            'item': 'Ancestral Water Drop'
        },
        'Temple of Fire': {
            'north': 'Shaded Abyss',
            'south': 'Sacred River',
            'east': 'Pit of Lions',
            'item': 'Eternal Torch'
        },
        'Shaded Abyss': {
            'south': 'Temple of Fire',
            'east': 'Earth Cave',
            'item': 'Shadow Amulet'
        },
        'Earth Cave': {
            'west': 'Shaded Abyss',
            'east': 'Windy Peak',
            'south': 'Pit of Lions',
            'item': 'Stone Totem'
        },
        'Windy Peak': {
            'west': 'Earth Cave',
            'south': 'Sun Sanctuary',
            'item': 'Condor Feather'
        },
        'Sun Sanctuary': {
            'north': 'Windy Peak',
            'south': 'Altar of Olympus',
            'west': 'Pit of Lions',
            'item': 'Sun Crystal'
        },
        'Pit of Lions': {},
        'Altar of Olympus': {
            'north': 'Sun Sanctuary',
            'west': 'Ancestral Village'
        }
    }
    # TODO: Set the player's starting room.
    current_room = 'Ancestral Village'
    inventory = []
    required_items = 6
    # TODO: Create the player's inventory.
    show_instructions()
    # TODO: Call the instruction function at the appropriate time.

     while True:
        show_status(current_room, inventory, rooms)

        command = input("Enter your move: ").strip().lower()
        parts = command.split()

        # Movement commands.
        if len(parts) == 2 and parts[0] == 'go':
            direction = parts[1]

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print("You moved to", current_room)

                # Trap room: the player loses.
                if current_room == 'Pit of Lions':
                    print("You entered the Pit of Lions!")
                    print("The lions caught you. Game Over!")
                    break

                # Villain room: check the inventory.
                if current_room == 'Altar of Olympus':
                    if len(inventory) == required_items:
                        print("You collected all 6 items!")
                        print("You defeated Zeus! Congratulations!")
                    else:
                        print("You faced Zeus without all 6 items.")
                        print("Zeus defeated you. Game Over!")
                    break
            else:
                print("You cannot go that way.")

        # Item collection commands.
        elif len(parts) >= 2 and parts[0] == 'get':
            item_name = ' '.join(parts[1:])

            if 'item' in rooms[current_room]:
                room_item = rooms[current_room]['item']

                if item_name == room_item.lower():
                    inventory.append(room_item)
                    del rooms[current_room]['item']
                    print("You collected", room_item)
                else:
                    print("That item is not in this room.")
            else:
                print("There is no item in this room.")

        # Invalid commands.
        else:
            print("Invalid command. Try go north or get item name.")

    print("Thank you for playing Mystical Elemental Island!")


if __name__ == "__main__":
    main()
