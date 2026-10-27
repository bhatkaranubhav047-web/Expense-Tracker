
expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spending")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter expense name: ")

        try:
            amount = float(input("Enter expense amount (₹): "))

            if amount <= 0:
                print("Please enter an amount greater than zero.")
            else:
                expenses.append({
                    "name": name,
                    "amount": amount
                })
                print("Expense added successfully!")

        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nYour Expenses:")
            for i, expense in enumerate(expenses, start=1):
                print(
                    f"{i}. {expense['name']} - "
                    f"₹{expense['amount']:.2f}"
                )

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total Spending: ₹{total:.2f}")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
