try:
    age=int(input("Enter your age in that: "))


    if age<0:
        raise ValueError("Age cannot be negative")
    elif age>0:
        print("Age is valid",age)
    
except ValueError as e:
    print("Error: ",e)

except Exception as e:
    print("An unexpected error occurred: ", e)