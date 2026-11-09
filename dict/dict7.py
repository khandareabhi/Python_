dict={
    "name": "abhi",
    "age": 12,
    "roll_no": 23,
    "marks": 90
}

total=0
for value in dict.values():
    print(value)
    

print("Marks are: ",dict["marks"])

if "marks" in dict:
    print("Marks are present in the dictionary")