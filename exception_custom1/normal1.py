
def checkage(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    else:
        print("Age is valid: ",age)


try:
    age =int (input("Enter your age: "))
    checkage(age)

except ValueError as e:  # add the custom exception class name here
    print("Error: ",e)  

except Exception as e:
    print("Erro: ",e)

except KeyboardInterrupt:
    print("User interrupted the program.")  

except EOFError:
    print("End of file error occurred.")

except TypeError as e:
    print("Type Error: ", e)