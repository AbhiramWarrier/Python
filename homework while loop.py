password = "test"
user_input = input("Guess the password: ")

attempts = 0
while attempts< 3:
    
  if user_input  !=  password: 
     print("wrong password, try again two attempts left")
     
     user_input = input("Guess the password: ")
  
     
  attempts = 1

  if user_input != password:
     print("the password is wrong again")
  
     user_input = input("Guess the password: ")
  
    
  attempts = 2
  if user_input != password:
     print("you are out of attempts, restart and try again ")  
  else:

     print ("you guessed the password right congratulations")
  attempts = 3
