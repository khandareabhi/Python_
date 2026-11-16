arr=[1,2,3,5,6,7,8,9]

print(type(arr))

for i in arr:
    if(i==5):
        break

    print(i) # print the elements of the list until the break statement is executed. The break statement will terminate the loop when the value of i is equal to 5.
