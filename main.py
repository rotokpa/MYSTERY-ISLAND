import time 
from game import (
    get_available_moves,
    move_player,
    show_location,
    check_for_item,
    show_inventory
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

    while True:
        show_location(player)

        available_moves = get_available_moves(player["location"])

        print("\nAvailable destinations:")

        for destination in available_moves:
            print(f"- {destination}")

        print("\nEnter Q to quit.")
        print("Enter I to check your inventory.")

        choice = input("Where would you like to go? ").strip()

        if choice.lower() == "q":
            print("\nThank you for playing Mystery Island!")
            break

        destination = choice.title()
        if choice.lower() == "i":
            show_inventory(player)
            continue
        

        if move_player(player, destination):
            print(f"\nYou successfully moved to {destination}!")
            print(f"Remaining energy: {player['energy']}")
            
            if check_for_item(player):
                collected_item = player["inventory"][-1]
                print(f"You collected the {collected_item}!")


            if player["energy"] == 0:
                print("\nYou have run out of energy!")
                print("\nGAME OVER!")
                print("\nYou Lost!")
                break
        else:
            if player["energy"] == 0:
                print("\nYou have run out of energy!")
                print("\nGAME OVER!")
                print("\nYou Lost!")
                break

            if destination == "Old Bridge" and "Rope" not in player["inventory"]:
                ( print("\nYou need a Rope to cross the Old Bridge!!!!"))

            elif destination == "Lighthouse" and "Lantern" not in player["inventory"]:
                print("\nYou need a Lantern to restore the Lighthouse!")

            else:
                print("\nYou cannot move there. Please choose an available destination.")
start_game()

