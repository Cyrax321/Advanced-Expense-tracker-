import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description, date=None):
        if date is None:
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.expenses.append({"amount": amount, "category": category, "description": description, "date": date})

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("\nAll Expenses:")
        for index, expense in enumerate(self.expenses, start=1):
            print(f"ID: {index}, Amount: ${expense['amount']:.2f}, Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")

    def view_expenses_by_category(self, category):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print(f"\nExpenses in Category '{category}':")
        for index, expense in enumerate(self.expenses, start=1):
            if expense['category'] == category:
                print(f"ID: {index}, Amount: ${expense['amount']:.2f}, Description: {expense['description']}, Date: {expense['date']}")

    def delete_expense(self, expense_id):
        if expense_id <= 0 or expense_id > len(self.expenses):
            print("Invalid expense ID.")
            return
        del self.expenses[expense_id - 1]
        print("Expense deleted successfully!")

    def clear_expenses(self):
        self.expenses = []
        print("All expenses cleared successfully!")

    def filter_expenses_by_date_range(self, start_date, end_date):
        start_datetime = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_datetime = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        if not self.expenses:
            print("No expenses recorded.")
            return
        print(f"\nExpenses between {start_date} and {end_date}:")
        for index, expense in enumerate(self.expenses, start=1):
            expense_date = datetime.datetime.strptime(expense['date'], "%Y-%m-%d %H:%M:%S")
            if start_datetime <= expense_date <= end_datetime:
                print(f"ID: {index}, Amount: ${expense['amount']:.2f}, Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")

    def calculate_total_expenses(self):
        total_expenses = sum(expense['amount'] for expense in self.expenses)
        print(f"\nTotal Expenses: ${total_expenses:.2f}")

def main():
    expense_tracker = ExpenseTracker()

    print("*" * 50)
    print("        Expense Tracker (built by CyRax)        ")
    print("*" * 50)

    while True:
        print("\nOptions:")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View expenses by category")
        print("4. Filter expenses by date range")
        print("5. Calculate total expenses")
        print("6. Delete expense by ID")
        print("7. Clear all expenses")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nEnter expense details:")
            amount = float(input("Amount ($): "))
            category = input("Category: ")
            description = input("Description: ")
            expense_tracker.add_expense(amount, category, description)
            print("\nExpense added successfully!")
        elif choice == "2":
            expense_tracker.view_expenses()
        elif choice == "3":
            category = input("\nEnter category to view expenses: ")
            expense_tracker.view_expenses_by_category(category)
        elif choice == "4":
            start_date = input("\nEnter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            expense_tracker.filter_expenses_by_date_range(start_date, end_date)
        elif choice == "5":
            expense_tracker.calculate_total_expenses()
        elif choice == "6":
            expense_id = int(input("\nEnter expense ID to delete: "))
            expense_tracker.delete_expense(expense_id)
        elif choice == "7":
            expense_tracker.clear_expenses()
        elif choice == "8":
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice")

if __name__ == "__main__":
    main()
