# 💰 Personal Budget Tracker

A simple command-line tool to help you log income and expenses, view spending summaries by category, and track your overall financial balance. Built with Python using basic data structures and modules for persistence and timestamping.

---

## 🚀 Features

- Add income and expense transactions
- View total balance and category-wise expense summary
- Save and load transactions from a JSON file
- Timestamp each transaction automatically
- Input validation for safe and clean data entry

---

## 🧱 How It Works

### Data Structure
- Transactions are stored as a list of dictionaries:
  ```python
  transactions = [
      {
          "type": "expense",
          "amount": 50.0,
          "category": "Food",
          "note": "Lunch",
          "date": "2025-11-04T08:30:00"
      },
      ...
  ]
  ```

- Summary is computed as a dictionary:
  ```python
  summary = {
      "Food": 120.0,
      "Transport": 45.0
  }
  ```

---

## 📦 Requirements
- Python 3.7+
- No external libraries required

---

## 🛠️ Usage
- Clone or download the repository.
- Run the script:
  ```bash
  python budget_tracker.py
  ```
- Use the menu to:
  - Add Expense
  - Add Income
  - View Summary
  - Quit (saves data to transactions.json)

---

## 📂 File Structure
```
budget_tracker/
├── Personal budget_tracker.py
├── transactions.json  # auto-generated
└── README.md
```

---

## 🧪 Example Flow
```
Welcome to Personal Budget Tracker!

1. Add Expense
2. Add Income
3. View Summary
4. Quit

Choose an option: 1
Enter amount: 50
Enter category: Food
Enter note (optional): Lunch
Expense added!

Choose an option: 3
Balance: ₹-50.00
Spending by category:
- Food: ₹50.00
```

---

## 🧠 Core Concepts Used
- Lists and dictionaries for data modeling
- Loops for aggregation
- try...except for input validation
- json for saving/loading data
- datetime for timestamps

---

## 📈 Future Enhancements
- Edit or delete transactions
- Export summary to CSV
- Monthly budget alerts
- Graphical interface or web dashboard

---

## 👨‍💻 Author
Built by Rishav — passionate about practical AI/ML projects and productivity tools!