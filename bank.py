
name = input("Enter account holder name: ")
account_number = int(input("Enter account number: "))
pin = int(input("Set your 4-digit PIN: "))
balance = 0

while True:
    print("\n--- Banking System ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Account Holder:", name)
        print("Account Number:", account_number)
        print("Balance:", balance)

    elif choice == 2:
        entered_pin = int(input("Enter PIN: "))

        if entered_pin == pin:
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print("Amount deposited successfully!")
            else:
                print("Invalid amount!")
        else:
            print("Incorrect PIN!")

    elif choice == 3:
        entered_pin = int(input("Enter PIN: "))

        if entered_pin == pin:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Enter a valid amount!")
            elif amount > balance:
                print("Insufficient balance!")
            else:
                balance -= amount
                print("Amount withdrawn successfully!")
        else:
            print("Incorrect PIN!")

    elif choice == 4:
        print("Thank you for visiting!")
        break

    else:
        print("Invalid choice!")
