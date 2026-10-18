num=int(input("Enter the value: "))

i=0
sum=0

while(i<num):
    rev=num%10
    sum=sum+rev
    num=num//10

print(sum)
