
from game import (
    get_available_moves,
    move_player,
    show_location,
    check_for_item,
    show_inventory,
    rest_player
)


def start_game():
    print("==============================")
    print("       MYSTERY ISLAND")
    print("      THE LOST LIGHTHOUSE")
    print("==============================")

    player_name = input("Enter your name: ")

    print(f"\nWelcome, {player_name}!")

    player = {
        "name": player_name,
        "location": "Beach",
        "energy": 5,
        "inventory": []
    }

    print("You have awakened on a mysterious island.")
    print("Your mission is to restore the lighthouse.")

    game_completed = False

    while True:

        # Handle exhaustion before showing the normal menu.
        if player["energy"] == 0:
            print("\nYou are exhausted!")
            print("You must rest before moving again.")
            print("\nEnter R to rest and recover 1 energy.")
            print("Enter Q to quit.")

            choice = input("Your choice: ").strip().lower()

            if choice == "r":
                rest_player(player)
                continue

            elif choice == "q":
                print("\nThank you for playing Mystery Island!")
                break

            else:
                print("\nInvalid choice. Enter R or Q.")
                continue

        # Show the player's current location.
        show_location(player)

        available_moves = get_available_moves(player["location"])

        print("\nAvailable destinations:")

        for destination in available_moves:
            print(f"- {destination}")

        print("\nEnter Q to quit.")
        print("Enter I to check your inventory.")

        choice = input("Where would you like to go? ").strip()

        # Handle quitting.
        if choice.lower() == "q":
            print("\nThank you for playing Mystery Island!")
            break

        # Handle inventory.
        if choice.lower() == "i":
            show_inventory(player)
            continue

        destination = choice.title()

        # Handle movement.
        if move_player(player, destination):
            print(f"\nYou successfully moved to {destination}!")
            print(f"Remaining energy: {player['energy']}")

            # Check whether the player collected an item.
            if check_for_item(player):
                collected_item = player["inventory"][-1]
                print(f"You collected the {collected_item}!")

            # Handle the Lighthouse mission.
            if player["location"] == "Lighthouse":

                while True:
                    print("\nYou have reached the Lighthouse!")
                    print("Press S to switch on the Lighthouse.")

                    choice = input("Your choice: ").strip().lower()

                    if choice == "s":
                        print("\nThe Lighthouse begins to shine!")
                        print("MISSION COMPLETED!")
                        print("You have restored the light.")

                        game_completed = True
                        break

                    else:
                        print("Invalid choice. Please press S.")

                # Exit the main game loop after completing the mission.
                if game_completed:
                    break

        else:
            # Explain why a restricted location cannot be entered.
            if (
                destination == "Old Bridge"
                and "Rope" not in player["inventory"]
            ):
                print("\nYou need a Rope to cross the Old Bridge!")

            elif (
                destination == "Lighthouse"
                and "Lantern" not in player["inventory"]
            ):
                print("\nYou need a Lantern to restore the Lighthouse!")

            else:
                print(
                    "\nYou cannot move there. "
                    "Please choose an available destination."
                )


start_game()
