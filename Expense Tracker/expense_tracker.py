expenses = {}

# Function to add an expense.

def add_expense():
    amount = float(input("Enter expense amount :"))
    category = input("Enter expense category :")
    description = input("Enter Description :")

    expense = {
        "amount " : amount,
        "category" : category,
        "description" : description
    }
   

    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0 :
        print("No expenses found.")

    else :
        print("\n======= YOUR EXPENSES =======")

        for i, expense in enumerate(expenses, start=1):
            print(f"\nExpense {i}:")
            print("Amount :", expense["amount"])
            print("Category :", expense["category"])
            print("Description :", expense["description"])


def total_expense():

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expense :",total)


def delete_expense():
    if len(expenses) == 0:
        print("No expenses to delete.")
        return 
        
    view_expenses()

    number = int(input("\nEnter expense number to delete: "))

    if number >= 1 and number <= len(expenses) :
        expenses.pop(number - 1)
        print("Expense deleted successfully!")

    else :
        print("Invalid expense number.")


while True :
    print("\n =================================")
    print("       EXPENSE TRACKER")
    print("1. Add Expense.")
    print("2. View Expenses.")
    print("3. Calculate Total Expense.")
    print("4. Delete Expense.")
    print("5. Exit.")

    choice = input("\nEnter your choice :")

    if choice == '1':
        add_expense()

    elif choice == '2':
        view_expenses()

    elif choice == '3':
        total_expense()

    elif choice == '4':
        delete_expense()

    elif choice == '5':
        print("Thank you for using Expense Tracker.")
        break

    else :
        print("Invalid choice.")
        
