balance = 1000

def check_balance():
    print(f"Your current balance is {balance}")
    print("==============================")


def deposit(amount):
    global balance 
    if amount > 0 :
       balance += amount
    else :
        print("Cannot deposit a negative or zero amount.")
        print("==========================")


def withdraw(amount):
    global balance 
    if amount <= 0:
        print("Cannot withdraw a negative or zero amount.")
        print("=======================")
    elif amount > balance :
        print("Cannot withdrawing.Insufficient balance.")
        print("===============================")
    else :
        balance -= amount



if __name__ == "__main__" :
    print("=============================")
    print("Welcome to ABC Banking")
    print("=============================")
    print()



    while True :
        print("1. Check your balance .")
        print("2.Deposit an amount")
        print("3. Withdraw an amount.")
        print("4. Quit.")
        choice = int(input("Enter your Choice(1-4) :"))

        if choice == 1 :
            check_balance()
        elif choice == 2 :
            amt = float(input("Enter the amount to deposit :"))
            deposit(amt)
            print(f"Amount {amt} deposited successfully.")
        elif choice == 3 :
            amt = float(input("Enter the amount to withdraw :"))
            withdraw(amt)
            print(f"Amount {amt} withdrawn successfully.")
        elif choice == 4 :
            print("Quiting, have a nice day.")
            break
        else :
            print("Invalid choice!! Re-try.")
            print("================================")


print()
print("Thankyou for banking with us.")

