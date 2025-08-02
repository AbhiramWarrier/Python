thought_number = 17
guess = int(input("this is a number guessing game i am thinking of a number between 1 and 100"))
  
while guess != thought_number:
    
    if guess < thought_number:
        print("guess higher")
    elif guess > thought_number:
        print("guess lower")
    guess = int(input("try again with a new number"))

   
