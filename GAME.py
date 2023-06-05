import random
list = ["paper", "scissor", "rock"]
while True:
    user1=random.choice(list)
    computer="The computer showed {}"
    GAMER_input=input("enter 'rock' OR 'paper' OR 'Scissor'")
    if GAMER_input == user1:
        print(computer.format(user1) + " TIE")
    elif GAMER_input == "rock" and user1 == "paper":
        print(computer.format(user1) + " You lose")
    elif GAMER_input == "rock" and user1=="scissor":
        print(computer.format(user1) + " You win")       
    elif GAMER_input == "paper" and user1=="scissor":
        print(computer.format(user1) + " You You lose")     
    elif GAMER_input == "paper" and user1== "rock":
        print(computer.format(user1) + " You win")     
    elif GAMER_input == "scissor" and user1=="rock":
        print(computer.format(user1) + " You lose")   
    elif GAMER_input == "scissor" and user1=="paper":
        print(computer.format(user1) + " You win")
    else:
        print("invalid input")           