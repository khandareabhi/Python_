dict={
    "name":"Abhi",
    "age":12,
    "city":"pune",
    "country":"india"
}

dict.pop("country")

for key,value in dict.items():
    print(key,":",value)


print(type(dict))