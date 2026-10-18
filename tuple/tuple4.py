tuple2=(5,6,7,8,9,10)

print(type(tuple2))

print(tuple2)

list1=list(tuple2)

list1.append(11)

list1.insert(2,101)

tuple2=tuple(list1)

print(type(tuple2))

print(tuple2)