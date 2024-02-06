import random
user_name = input("Enter Your name:")
print(f"Good Luck {user_name}")
n = int(input("please enter rounds number:"))
user_win = 0
computer_win = 0
rounds = 1

while rounds <= n:
   print(f"Round: {rounds}")
   user_select = input("Please choose one snake-s, water-w, gun-g:")
   item = ["s","w","g"]
   computer_select = random.choice(item)
   print(computer_select)
   
   if user_select != 's' and user_select != 'w' and user_select != 'g':
      print("Invalid input,try again")
   
   if computer_select == 's':
      if user_select == 'w':
         computer_win += 1

      else:
         user_win += 1
   elif computer_select == 'w':
      if user_select == 'g':
         computer_win += 1
      else:
         user_win += 1
   elif computer_select == 'g':
      if user_select == 's':
         computer_win += 1
      else:
         user_win += 1
    
   if user_win > computer_win:
      print(f"you won Round {rounds} ")
   elif user_win < computer_win:
      print(f"Computer win round {rounds}")
   else:
      print("It's draw")
   rounds += 1 
print(user_win)
print(computer_win)       
if user_win == computer_win:
   print("It's draw")
elif user_win > computer_win:
   print("You win")
else:
   print("You lose")
   
      






