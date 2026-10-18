arr=[2,3,4,5,6,7,8,89,2]

seen=set()

for i in arr:
    if i in seen:
        print("Duplicate found: ",i)
        break
    seen.add(i)