arr=[2,3,4,5,6,7,8,9,10]

for i in arr:
    if(i%2==0):
        print(i)
    elif(i%2!=0):
        continue
    else:
        print("Invalid input")