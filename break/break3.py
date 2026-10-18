arr=[2,3,4,5,6,7,8,89]

target=int(input("Enter a number: "))

for i in arr:
    if(i==target):
        print("Found the target number: ",target)
        break
else:
    print("Target number not found: ",target)