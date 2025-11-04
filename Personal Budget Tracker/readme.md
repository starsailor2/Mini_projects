# Personal Budget Tracker

A simple command-line application to track your personal income and expenses. This Python-based budget tracker helps you monitor your financial transactions and view your portfolio balance.

## Features

- 📊 **View Portfolio**: Display all income and expenses with totals and net balance
- 💰 **Add Income**: Record income with amount, type, and timestamp
- 💸 **Add Expense**: Record expenses with amount, category, and timestamp
- 💾 **Data Persistence**: All data is saved to a JSON file for future sessions
- ⏰ **Timestamps**: Each transaction is recorded with time (HH:MM:SS format)

## Requirements

- Python 3.6 or higher
- No external libraries required (uses built-in modules)

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd "Personal Budget Tracker"
   ```

## Usage

Run the application:
```bash
python main.py
```

### Menu Options

1. **View Portfolio** - Shows all your income and expenses with totals
2. **Add Expense** - Add a new expense entry
3. **Add Income** - Add a new income entry
4. **Exit** - Quit the application

### Example Usage

```
Welcome to the Personal Budget Tracker!
1. View Portfolio
2. Add Expense
3. Add Income
4. Exit
Please enter your choice (1-4): 3

Enter income amount: 5000
Enter income type (e.g., Salary, Gift): Salary
Income added...
```

## Data Storage

All data is stored in `Student.json` in the same directory as the script. The file is automatically created on first run.

### JSON Structure
```json
{
    "income": [
        {
            "amount": 5000.0,
            "type": "Salary",
            "timestamp": "14:30:45"
        }
    ],
    "expense": [
        {
            "amount": 150.0,
            "category": "Food",
            "timestamp": "15:20:10"
        }
    ]
}
```

## Project Structure

```
Personal Budget Tracker/
│
├── main.py          # Main application file
├── Student.json     # Data storage (auto-generated)
└── README.md        # This file
```

## Functions Overview

- `load_income()` - Loads income data from JSON file
- `load_expense()` - Loads expense data from JSON file
- `update_income()` - Saves income data to JSON file
- `update_expense()` - Saves expense data to JSON file
- `add_income()` - Prompts user to add new income entry
- `add_expense()` - Prompts user to add new expense entry
- `view_portfolio()` - Displays complete financial summary
- `menu()` - Displays main menu options
- `main()` - Main program loop

## Error Handling

- Invalid amount inputs are caught and user is prompted again
- Missing JSON file is automatically created
- Empty or corrupted data gracefully handled with default values

## License

This project is open source and available for personal and educational use.

## Author

Created as a mini project for learning Python file handling and JSON operations.