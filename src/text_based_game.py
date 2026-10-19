"""Project Two starter for the student's text-based adventure game."""

# Author: Abel Antonio Cardenas Jaimes


def show_instructions():
    """Display the game objective and available commands."""
    print("Welcome to Mystical Elemental Island!")
    print("Collect all 6 items before facing Zeus.")
    print("Move commands: go north, go south, go east, go west")
    print("Collect items: get <item name>")
    print("Be careful! The Pit of Lions sends you back to the start.")


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("-------------------------")
    print("You are in", current_room)
    print("Inventory:", inventory)

    if 'item' in rooms[current_room]:
        print("You see", rooms[current_room]['item'])


def main():
    """Run the main gameplay loop."""
    rooms = {
    'Great Hall': {'south': 'Bedroom'},
    'Bedroom': {'north': 'Great Hall'}
}

    # TODO: Set the player's starting room.

    # TODO: Create the player's inventory.

    # TODO: Call the instruction function at the appropriate time.

    # TODO: Create the gameplay loop.
    # Within the loop:
    #   - Show player status.
    #   - Prompt for the player's next command.
    #   - Handle valid movement commands.
    #   - Handle valid get-item commands.
    #   - Validate invalid commands.
    #   - Update room/inventory state when appropriate.
    #   - Detect and display the required winning outcome.
    #   - Detect and display the required losing outcome.
    #   - End the loop when the player has won or lost.
    pass


if __name__ == "__main__":
    main()
