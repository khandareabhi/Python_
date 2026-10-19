s=input("Enter a String: ")

count=0

for ch in s.lower():
    if ch in "aeiou":
        count+=1

print("Vowels: ",count)