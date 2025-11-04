import os
import json
import time

JSON_FILE = os.path.join(os.path.dirname(__file__), 'Student.json')

def load_expense():
    global expense
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as f:
            data = json.load(f)
            expense = data.get("expense", [])
    else:
        expense = []

def load_income():
    global income
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as f:
            data = json.load(f)
            income = data.get("income", [])

    else:
        income = []

def update_income():
    global income, expense
    # i am preserving expense data when updating income
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as f:
            data = json.load(f)
            expense = data.get('expense', [])

    with open(JSON_FILE, 'w') as f:
        data = {'income': income, 'expense': expense}
        json.dump(data, f, indent=4)

def update_expense():
    global income, expense
    # i am preserving income data when updating expense
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as f:
            data = json.load(f)
            income = data.get('income', [])
    
    with open(JSON_FILE, 'w') as f:
        data = {'income': income, 'expense': expense}
        json.dump(data, f, indent=4)

def view_portfolio():
    load_income()
    load_expense()

    print("Viewing portfolio...")
    print("Income:")

    for item in income:
        print(f" - {item['type']}: ${item['amount']:.2f}")
    print("Expenses:")
    for item in expense:
        print(f" - {item['category']}: ${item['amount']:.2f}")

    total_income = sum(item['amount'] for item in income)
    total_expense = sum(item['amount'] for item in expense)

    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Net Income: ${total_income - total_expense:.2f}")


def add_expense():
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    category = input("Enter expense category (e.g., Food, Transport): ")
    formatted_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
    expense.append({"amount": amount, "category": category, "timestamp": formatted_time})
    update_expense()
    print("Expense added...")

def add_income():
    while True:
        try:
            amount = float(input("Enter income amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    income_type = input("Enter income type (e.g., Salary, Gift): ")
    formatted_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
    income.append({"amount": amount, "type": income_type, "timestamp": formatted_time})
    update_income()
    print("Income added...")

def menu():
    print("Welcome to the Personal Budget Tracker!")
    print("1. View Portfolio")
    print("2. Add Expense")
    print("3. Add Income")
    print("4. Exit")

def get_user_choice():
    choice = input("Please enter your choice (1-4): ")
    return choice

income  = []
expense = []

def main():
    global income, expense

    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'w') as f:
            json.dump({"income": [], "expense": []}, f, indent=4)  # loading empty lists in startup
        print(f"Created new data file: {JSON_FILE}")

    load_income()
    load_expense()

    while True:
        menu()
        choice = get_user_choice()

        if choice == '1':
            view_portfolio()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            add_income()
        elif choice == '4':
            print("Exiting the Personal Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()