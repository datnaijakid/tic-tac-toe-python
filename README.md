# Tic-Tac-Toe Game

This repository contains a simple command-line implementation of the classic Tic-Tac-Toe game in Python. The game allows two players to take turns placing their marks (X and O) on a 3x3 grid until one player wins or the game ends in a draw.

## Features

- **Two-Player Mode**: Players take turns to place their marks on the grid.
- **Win Detection**: The game checks for a winner after each turn.
- **Draw Detection**: The game detects if all spaces are filled without a winner, resulting in a draw.
- **User -Friendly Interface**: The game displays the current state of the board after each turn.

## How to Play

1. Clone the repository:
   ```bash
   git clone https://github.com/datnaijakid/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. Run the game:
   ```bash
   python tic_tac_toe.py
   ```

3. Follow the prompts to enter your moves. Players will be asked to specify the position where they want to place their mark (X or O).

## Game Board Layout

The game board is represented as follows:

```
   a     b     c
      |     |     
1  -  |  -  |  -  
 _____|_____|_____
      |     |     
2  -  |  -  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  -  
      |     |     
```

- Players can choose positions using the format (e.g., `a1`, `b2`, `c3`).

## Technologies Used

- **Python**: The programming language used to develop the game.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
