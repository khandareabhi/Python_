dict={
    "abhi":[50,40,60],
    "ram":[80,90,10],
    "sam":[70,60,30],
}

count=0
for name,value in dict.items():
    total=sum(value)

    avg=total/3

    if(avg>90):
        grade="O Grade"
    elif(avg>80):
        grade="A++ Grade"
    elif(avg>75):
        grade="A grade"
    elif(avg>50):
        grade="B grade"
    elif(avg>35):
        grade="C grade"
    elif(avg<35):
        grade="Fail"

    print("----------------------------------")
    print("Name of Student",name)
    print("Total marks of that: ",total)
    print("Avg of that ",avg)
    print("Grade of that: ",grade)

