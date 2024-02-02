import random

username = input("Enter your name:")
print(f"Good luck {username}")

game = ["snake","water","gun"]
computer_select = random.choice(game)
print(computer_select)

user_select = input("Please select one snake,water,gun:")
if(user_select == computer_select):
    print("It's Draw, try again")
elif(user_select == "snake"):
    if(computer_select == "water"):
        print("Snake drinks water, you win")
    else:
        print("Gun will kill the snake, you lose")
elif(user_select == "water"):
    if(computer_select == "gun"):
        print("Gun will drown in water, you win")
    else:
        print("snake drinks water, you lose")
elif(user_select == "gun"):
    if(computer_select == "snake"):
        print("Gun will kill the snake, you win")
    else:
        print("Gun will drown in water, you lose")


