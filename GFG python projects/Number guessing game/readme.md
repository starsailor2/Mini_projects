# Number Guessing Game

A fun and interactive command-line number guessing game built with Python. Test your intuition and logic skills by guessing the randomly generated number within a limited number of attempts!

## Features

- **Multiple Difficulty Levels**: Choose from Easy, Medium, or Hard modes
- **Input Validation**: Handles invalid inputs and out-of-range guesses
- **Attempt Tracking**: Shows remaining attempts after each guess
- **Score System**: Tracks your best performance across multiple games
- **Statistics**: Displays games played and best scores
- **Replay Option**: Play multiple rounds without restarting the program
- **Smart Hints**: Get feedback if your guess is too high or too low

## Game Modes

| Difficulty | Range   | Attempts |
|-----------|---------|----------|
| Easy      | 1-50    | 15       |
| Medium    | 1-100   | 10       |
| Hard      | 1-200   | 7        |

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Installation

1. Clone or download this repository
2. Navigate to the game directory:
```bash
cd "GFG python projects/Number guessing game"
```

## How to Play

1. Run the game:
```bash
python main.py
```

2. Select your difficulty level (1-3)

3. Enter your guesses when prompted

4. Try to guess the number in as few attempts as possible!

5. After each game, you can choose to play again or exit

## Gameplay Example

```
==================================================
WELCOME TO THE NUMBER GUESSING GAME!
==================================================

=== Select Difficulty ===
1. Easy (1-50, 15 attempts)
2. Medium (1-100, 10 attempts)
3. Hard (1-200, 7 attempts)
Choose difficulty (1-3): 2

Guess the number between 1 and 100
You have 10 attempts!

Attempt 1/10 - Enter your guess: 50
Too high! 9 attempts remaining.
Attempt 2/10 - Enter your guess: 25
Too low! 8 attempts remaining.
Attempt 3/10 - Enter your guess: 37

Congratulations! You guessed it in 3 attempt(s)!
New best score: 3 attempts!

Stats: Games played: 1 | Best score: 3

Play again? (y/n): n

Thanks for playing! Goodbye!
```

## Code Structure

- `get_valid_input()`: Validates and returns user input
- `select_difficulty()`: Handles difficulty selection
- `play_game()`: Main game loop and logic
- `main()`: Program entry point with replay functionality

## Tips for Playing

1. Start with a guess in the middle of the range
2. Use binary search strategy for optimal performance
3. Pay attention to "too high" or "too low" hints
4. Track your mental range after each guess

## Future Enhancements

Potential features for future versions:
- Save high scores to a file
- Add a hint system (costs attempts)
- Implement a leaderboard
- Add a timer mode for speedrun challenges
- GUI version using tkinter
- Multiplayer mode

## License

This project is open source and available for educational purposes.

## Author

Created as part of the GFG Python Projects collection.

## Contributing

Feel free to fork this project and submit pull requests for any improvements!