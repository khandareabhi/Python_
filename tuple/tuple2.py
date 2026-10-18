tuple1=(21,2,4,6,7,8,7,9,10,11,12,3)

print(type(tuple1))


list1=list(tuple1)

list1.insert(2,101)
list1.append(13)
list1.sort()

tuple1=tuple(list1)

print(tuple1)
