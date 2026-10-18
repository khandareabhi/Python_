num=int(input("Enter a number: "))
ar=[]
total=0

for i in range(num):
    num1=int(input("Enter a number: "))
    ar.append(num1)


print(ar)

for i in ar:
    if i<0:
        continue
    total+=i


print(total)