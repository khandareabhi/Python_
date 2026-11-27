
class AgeinvalidError(Exception):
    pass


def validate_age(age):
    if age<0:
        raise AgeinvalidError("Age cannnot be negative")
    elif age>0:
        print("Age is valid",age)

try:
    age = int(input("Enter your age: "))
    validate_age(age)
except AgeinvalidError as e:
    print("Error: ",e)

