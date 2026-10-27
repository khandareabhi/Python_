class Bank:

    def __init__(self,name,account_number,balance=0):
        self.name=name
        self.account_number=account_number
        self.balance=balance

    
    def check_balance(self):
        print("Account Holder: ",self.name)
        print("Account Number: ",self.account_number)
        print("Balance : ",self.balance)
    
    def deposit(self,amount):
        if(amount>0):
            self.balance+=amount
            print("Amount Deposit successfully")
        else:
            print("Invalid amount!")
    
    def withdraw(self,amount):
        if amount<=0:
            print("Enter valid amount!")
        elif amount>self.balance:
            print("Insufficient Amount")
        else:
            self.balance-=amount
            print("Amount withdraw sucessfully")


name=input("Enter the account holder name:")
account_number=int(input("Enter the account number: "))

account = Bank(name,account_number)

while True:
    print("\n---Banking_System ---")
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        account.check_balance()
    
    elif choice==2:
        amount=float(input("Enter the value : "))
        account.deposit(amount)
    
    elif choice==3:
        amount=float(input("Enter the value: "))
        account.withdraw(amount)

    elif choice==4:
        print("thank you for visiting")
        break
    
    else:
        print("invalid output")
    


