LOCATION_MAP = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"]
}

LOCATION_ITEMS = {
    "Beach": "Rope",
    "Cave": "Lantern"
}

def get_available_moves(location):
    if location in LOCATION_MAP:
        return LOCATION_MAP[location]
    else:
        return []

def move_player(player, destination):
    if player["energy"] <= 0:
        return False

    current_location = player["location"]

    available_moves = get_available_moves(current_location)

    if destination in available_moves and can_access_location(player, destination):
        player["location"] = destination
        player["energy"] -= 1
        return True
    else:
        return False

def show_location(player):
    player_location = player["location"]
    print(f"You are currently at {player_location}")


def collect_item(player, item):
    if item in player["inventory"]:
        return False

    player["inventory"].append(item)

    return True


def get_item_at_location(location):
    return LOCATION_ITEMS.get(location)


def check_for_item(player):
    player_location = player["location"]
    find_item = get_item_at_location(player_location)

    if find_item is None:
        return False
    
    return collect_item(player, find_item)


def show_inventory(player):
    inventory = player["inventory"]

    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Items in your inventory:")
        for item in inventory:
            print(f"- {item}")

def can_access_location(player, destination):
    if destination == "Old Bridge":
        return "Rope" in player["inventory"]

    elif destination == "Lighthouse":
        return "Lantern" in player["inventory"]

    return True

import time

def rest_player(player):
    print("You are resting...")

    for number in range(5, 0, -1):
        print(number)
        time.sleep(1)

    player["energy"] = min(player["energy"] + 1, 5)

    print(f"Recovered energy: {player['energy']}")