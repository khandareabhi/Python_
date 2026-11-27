
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
num=int(input("Enter a number to find its factorial: "))
n=factorial(num)
print("Factorial of",num," is:",n)