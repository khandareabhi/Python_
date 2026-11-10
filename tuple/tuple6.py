tuple1=(1,2,3,5,7,5)

print(type(tuple1))

tuple2=list(tuple1)

tuple2.append(6)
tuple2.append(5)


tuple1=tuple(tuple2)

print(tuple1)