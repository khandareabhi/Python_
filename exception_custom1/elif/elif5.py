num=int(input("Enter a number: "))

for i in range(1, num):

    if(i%2==1):
        print(i)
    elif(i%2==0):
        continue
    else:
        print("Invalid input")