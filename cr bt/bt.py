import json
import os


def load_transactions(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return {"income": [], "expenses": []}


def save_transactions(transactions, filename):
    with open(filename, 'w') as file:
        json.dump(transactions, file)


def add_income(transactions):
    category = input("Enter income category: ")
    amount = float(input("Enter income amount: "))
    transactions["income"].append({"category": category, "amount": amount})


def add_expense(transactions):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    transactions["expenses"].append({"category": category, "amount": amount})


def calculate_budget(transactions):
    total_income = sum(transaction["amount"] for transaction in transactions["income"])
    total_expenses = sum(transaction["amount"] for transaction in transactions["expenses"])
    remaining_budget = total_income - total_expenses
    return remaining_budget


def analyze_expenses(transactions):
    expense_categories = {}
    for expense in transactions["expenses"]:
        category = expense["category"]
        amount = expense["amount"]
        if category in expense_categories:
            expense_categories[category] += amount
        else:
            expense_categories[category] = amount
    print("\nExpense Analysis:")
    for category, amount in expense_categories.items():
        print(f"{category}: ${amount}")


def main():
    filename = "transactions.json"
    transactions = load_transactions(filename)

    while True:
        print("\n===== PERSONAL BUDGET TRACKER =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_income(transactions)
        elif choice == "2":
            add_expense(transactions)
        elif choice == "3":
            remaining_budget = calculate_budget(transactions)
            print(f"\nRemaining Budget: ${remaining_budget}")
        elif choice == "4":
            analyze_expenses(transactions)
        elif choice == "5":
            save_transactions(transactions, filename)
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
