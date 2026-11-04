# Mystery Island — The Lost Lighthouse

A text-based adventure game built with Python.

## About the Game

You awaken on a mysterious island with one mission: restore the lost lighthouse.

Explore different locations, collect useful items, manage your energy, and overcome obstacles on your journey. To complete your mission, you must find the Rope and Lantern, reach the Lighthouse, and activate its switch.

Can you restore the light and complete your mission?

## Features

- **Island Exploration:** Travel between the Beach, Jungle, Cave, Old Bridge, and Lighthouse.
- **Energy System:** Every successful move costs 1 energy point.
- **Resting Mechanic:** Recover energy with a 5-second countdown when exhausted.
- **Item Collection:** Find and collect the Rope and Lantern.
- **Inventory System:** Check the items you have collected.
- **Location Requirements:** Use the Rope to cross the Old Bridge and the Lantern to access the Lighthouse.
- **Interactive Ending:** Activate the Lighthouse switch to complete the mission.

## Game Map

```text
Beach
  |
Jungle
  |
Cave
  |
Old Bridge
  |
Lighthouse
```

The locations are connected, allowing you to travel back to previous areas.

## Requirements

- Python 3
- No external Python packages are required.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/rotokpa/MYSTERY-ISLAND.git
   ```

2. Navigate into the project folder:

   ```bash
   cd MYSTERY-ISLAND
   ```

3. Run the game:

   ```bash
   python3 main.py
   ```

## How to Play

- Enter your name to begin.
- Type an available destination to move.
- Enter `I` to check your inventory.
- Enter `Q` to quit the game.
- Collect the Rope at the Beach.
- Collect the Lantern at the Cave.
- Use the required items to access restricted locations.
- When your energy reaches zero, rest to recover 1 energy point.
- Reach the Lighthouse and press `S` to activate the switch.

## Project Structure

```text
MYSTERY-ISLAND/
├── main.py
├── game.py
└── README.md
```

- `main.py` — Controls the main game loop, player choices, and mission completion.
- `game.py` — Contains the game functions for movement, items, inventory, energy, and location access.
- `README.md` — Documents the project and explains how to run and play the game.

## Concepts Practiced

This project helped me practice:

- Python functions
- Dictionaries and lists
- Conditional statements (`if`, `elif`, `else`)
- `while` and `for` loops
- User input and output
- Boolean values and return statements
- String methods
- Game state management
- Importing functions between Python modules

## Future Improvements

- Add more island locations and hidden areas.
- Introduce hazards and challenges.
- Add clues and puzzles.
- Improve the story and player experience.
- Add automated tests.

## Author

Built as a Python learning project.
