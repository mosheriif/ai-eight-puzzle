
# 8-Puzzle Solver

This repository contains a solution to the 8-puzzle problem using various search algorithms. This project is part of the (CSE351) Introduction to Artificial Intelligence course.

## Overview

The 8-puzzle consists of a 3x3 grid with eight numbered tiles and one blank space. The objective is to arrange the tiles in ascending order from 0 to 8 (where 0 represents the blank) by sliding tiles into the blank space, moving from an initial configuration to the goal state.

Given an initial state of the board, this program finds a sequence of moves to transition from the initial state to the goal state. The solution uses four different search algorithms to explore the search space of all possible tile configurations.

## Algorithms

This project implements the following search algorithms:

1. **Breadth-First Search (BFS)** - An uninformed search algorithm exploring nodes level by level.
2. **Depth-First Search (DFS)** - An uninformed search algorithm exploring nodes by depth.
3. **Iterative Deepening Depth-First Search (IDDFS)** - An uninformed search combining DFS with breadth control.
4. **A\*** - An informed search algorithm using heuristic functions for optimization.

### Heuristics

The A\* algorithm uses two heuristics for comparison:
- **Manhattan Distance**: The sum of the absolute differences between the current and goal positions of tiles.
- **Euclidean Distance**: The straight-line distance between the current and goal positions of tiles.

Each heuristic is analyzed for its admissibility based on the nodes expanded and the output paths.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/8-puzzle-solver.git
   cd 8-puzzle-solver
   ```

2. Run the code:
   Ensure you have Python installed and execute the following to start the program.
   ```bash
   python solver.py
   ```

## Usage

1. **Input**: The program starts from a random initial state of the 8-puzzle. The user can also provide custom starting configurations if needed.
2. **Output**: The program displays a traceable sequence of moves from the initial state to the goal state, with detailed information on:
   - Path to the goal
   - Cost of the path
   - Nodes expanded
   - Search depth
   - Execution time

## Deliverables

This repository contains:

- **Code**: Well-commented implementation of the 8-puzzle problem.
- **Report**: Documented analysis with sample runs, data structures used, explanations for each algorithm, performance comparison of heuristics, and assumptions.

## Notes

- **Language**: Python
- **Execution**: Run `solver.py` to initiate the solver with a random initial configuration or provide custom inputs.
- **Extras**: Enhanced visual output for tracing moves from the initial to the goal state.
