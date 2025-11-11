# FLAMES Game 🔥

A Python implementation of the classic FLAMES game that determines the relationship between two people based on their names.

## What is FLAMES?

FLAMES is a popular game among friends to determine the relationship status between two people. The acronym stands for:
- **F** - Friends
- **L** - Love
- **A** - Affection
- **M** - Marriage
- **E** - Enemies
- **S** - Siblings

## How It Works

1. **Input**: Enter two names
2. **Remove Common Characters**: All common characters between the two names are removed (one occurrence at a time)
3. **Count Remaining Characters**: The total number of remaining characters is calculated
4. **FLAMES Elimination**: Using the count, letters are eliminated from "FLAMES" in a circular manner
5. **Result**: The last remaining letter reveals the relationship!

## Algorithm

The game uses the **Josephus Problem** algorithm:
1. Start with the list `["F", "L", "A", "M", "E", "S"]`
2. Count `n` positions (where `n` = remaining characters count)
3. Remove the letter at that position
4. Continue counting from the next position
5. Repeat until only one letter remains

## Installation

No external dependencies required! Just Python 3.10+ (for `match-case` statement).

```bash
git clone <repository-url>
cd "Flames Game"
```

## Usage

Run the program:

```bash
python main.py
```

**Example:**

```
Enter first name: john
Enter second name: emily

# Common characters removed: None
# Remaining: "john" + "emily" = 9 characters
# Result: They are in Loooove ❤️
```

## Code Structure

- `common_characters_removal()`: Removes matching characters from both names
- Main loop: Implements the FLAMES elimination algorithm
- Match statement: Displays the relationship result

## Features

- Case-insensitive name input
- Accurate character matching and removal
- Fun relationship predictions
- Simple console-based interface

## Example Scenarios

| Name 1 | Name 2 | Result |
|--------|--------|--------|
| Alice  | Bob    | Varies based on algorithm |
| John   | Jane   | Varies based on algorithm |
| Tom    | Emma   | Varies based on algorithm |

## Notes

- This is a fun game and should not be taken seriously! 😄
- Results are based on mathematical calculations, not actual relationship compatibility
- The game is popular in schools and among friends for entertainment

## License

Free to use for educational and entertainment purposes.

## Contributing

Feel free to fork and improve the game! Possible enhancements:
- GUI interface
- Multiple rounds
- Statistics tracking
- Custom relationship categories

---

**Have fun playing FLAMES! 🎮**