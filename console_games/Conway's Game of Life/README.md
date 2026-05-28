Conway's Game of Life - Console Edition
A classic implementation of Conway's Game of Life in Python, visualized directly in the terminal.

Description
This project simulates cellular automaton devised by mathematician John Conway. The game evolves on a 2D grid where cells live, die, or reproduce based on their neighbors. The simulation runs in real-time within the console, using a toroidal grid (wrap-around edges).

Rules
Each cell follows these simple rules:

Birth – A dead cell with exactly 3 live neighbors becomes alive

Survival – A live cell with 2 or 3 live neighbors stays alive

Death – A live cell with fewer than 2 or more than 3 live neighbors dies

Features
Real-time console visualization using [ ] brackets

Toroidal grid (edges wrap around to the opposite side)

Configurable grid size (currently 10×10)

Pre‑loaded starting patterns (two independent gliders)

Requirements
Python 3.x

No external dependencies (uses only built‑in time module)
---
Author: Valionce
License: MIT