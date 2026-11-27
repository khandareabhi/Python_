set={2,3,4,5,6,7,8,9}

print(type(set))

print(set)

set.add(20)

set.remove(4)

print(set)   # cannot be accessed by index convert into the list then access by index

list=list(set)
print(list[2])
