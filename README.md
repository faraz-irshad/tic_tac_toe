# TIC TAC TOE - Pygame Implementation

This is a simple **Tic Tac Toe** game implemented using Python and Pygame. The game allows a player to compete against a computer with intelligent decision-making to block the player or secure a win. 

## Features

- Interactive graphical grid created using Pygame.
- Player uses the mouse to click on the grid to place their move.
- Computer makes intelligent moves to either win or block the player.
- Game supports replay after a match is complete.

## Requirements

- Python 3.x
- Pygame library

Install Pygame using pip if it’s not already installed:
```bash
pip install pygame
```
3. Run the game:
   ```bash
   git clone https://github.com/faraz-irshad/tic_tac_toe.git
   cd tic_tac_toe
   python3 tic_tac_toe.py
   
## Code Structure

### Main Components

- **Board Class**: Manages the game grid, marks moves, checks for a winner or draw, and declares results.
- **User Class**: Handles user interactions, including mouse clicks to select grid positions.
- **Computer Class**: Implements the computer's decision-making logic, including blocking the player or securing a win.

### Key Functions

- **display_grid**: Draws the Tic Tac Toe grid.
- **mark**: Places the player's or computer's symbol on the grid.
- **is_draw**: Checks if the game ends in a draw.
- **winning_condition**: Checks all possible winning combinations.
- **winner_declaration**: Displays the winner and provides an option to restart the game.
- **user_turn**: Handles the player's move.
- **computer_turn**: Handles the computer's move using strategic logic.

## Game Flow

1. **Toss**: Randomly determines who goes first (player or computer).
2. **Turns**: Alternates between the player and the computer until a win or draw is detected.
3. **Game Over**: Displays the result (win/draw) and allows restarting.

## Future Enhancements

- Add sound effects for moves and game events.
- Enhance the computer's AI with more advanced strategies.
- Add multiplayer mode for two players.
