# Shikaku Puzzle Game

This is a Python implementation of the popular Japanese logic puzzle game, Shikaku. The game is built using the Turtle graphics library and features a graphical user interface (GUI) for easy interaction.

## Project Structure

The project is organized into several Python files:

- `block.py`: Contains the Block and BlockManager classes which are used to manage the game blocks.
- `data.py`: Contains the data used in the game.
- `main.py`: The entry point of the application.
- `search.py`: Contains the Solver class which is used to solve the puzzle.
- `ui.py`: Contains the GUI class which is responsible for rendering the game interface and handling user interactions.

## How to Play

The game starts with a grid of squares, some of which contain numbers. The goal is to divide the entire area into rectangular or square blocks such that each block contains exactly one number and that number represents the area of the block.

## Features

- **Interactive GUI**: The game features a user-friendly graphical interface that makes it easy to play the game.
- **Hint System**: If you're stuck, you can use the hint system which uses a solver to provide a hint for the next move.
- **Multiple Solving Algorithms**: The game features multiple solving algorithms which you can choose from.

## Running the Game

To run the game, simply execute the `main.py` file:

```bash
python main.py
