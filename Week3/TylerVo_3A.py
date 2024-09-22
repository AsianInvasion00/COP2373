from functools import reduce

# Function to get expenses from the user
def get_expenses():
    expenses = {}
    while True:
        expense_type = input("Enter the type of expense (or type 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        try:
            amount = float(input(f"Enter the amount for {expense_type}: "))
            expenses[expense_type] = amount
        except ValueError:
            print("Please enter a valid number for the amount.")
    return expenses

# Function to calculate total, highest, and lowest expenses using reduce
def analyze_expenses(expenses):
    # Use reduce to calculate the total expense
    total_expense = reduce(lambda x, y: x + y, expenses.values())
    
    highest_expense = max(expenses.items(), key=lambda x: x[1])
    lowest_expense = min(expenses.items(), key=lambda x: x[1])

    # Displaying the results to the user
    print(f"\nTotal Expenses: ${total_expense:.2f}")
    print(f"Highest Expense: {highest_expense[0]} - ${highest_expense[1]:.2f}")
    print(f"Lowest Expense: {lowest_expense[0]} - ${lowest_expense[1]:.2f}")

# Main function to run the program
def main():
    expenses = get_expenses()
    if expenses:
        analyze_expenses(expenses)
    else:
        print("No expenses entered.")

main()