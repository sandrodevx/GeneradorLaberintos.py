# Maze Generator 🧩

Welcome to the **Maze Generator**! This Python project generates perfect mazes using a **Depth-First Search (DFS)** algorithm. A perfect maze is a maze that has exactly one solution and no inaccessible areas. This tool is perfect for learning about maze generation algorithms, solving mazes, or just having fun!

---

## Features

- **Maze Generation**: Creates a perfect maze using the Depth-First Search (DFS) algorithm.
- **Customizable Size**: You can easily adjust the size of the maze (rows and columns).
- **ASCII Visualization**: Displays the maze in the console using ASCII characters.
- **Randomness**: Every maze generated is unique due to the random nature of the algorithm.

---

## How It Works

The maze is generated using the following steps:

1. **Initialization**:
   - A grid of cells is created, where each cell represents a room in the maze.
   - All walls between cells are initially active (no paths are open).

2. **Depth-First Search (DFS)**:
   - A random cell is chosen as the starting point.
   - From the current cell, a random unvisited neighbor is selected.
   - The wall between the current cell and the neighbor is removed.
   - The neighbor is marked as visited and becomes the current cell.
   - The process repeats until all cells have been visited.

3. **Result**:
   - A perfect maze is generated, with exactly one path between any two cells.
