age = int(input("enter how old you are"))
for i in  range (10,18):
 age = i
 if 12<= age <=18:
    print("at ", age, "you are allowed to have a tattoo")
 else:
    print("you are not allowed to have a tattoo")
    for age in range (18,21):
     if 18<= age <= 21:
        print("at", age, "you are allowed to have alcahol")
else:
 print("you are not allowed to have alcahol")
