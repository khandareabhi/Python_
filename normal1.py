
def checkage(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    else:
        print("Age is valid: ",age)


try:
    age =int (input("Enter your age: "))
    checkage(age)

except ValueError as e:
    print("Error: ",e)