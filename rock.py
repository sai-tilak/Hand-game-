from random import randint

choice = ['rock','paper','scissors']
computer = choice[randint(0,2)]

print("welcome to the Rock  , Paper ,Scissors Game\n")
player = input("your choice:").lower()
print("computer chose:"+ computer)

if player == computer:
    print("Draw")
elif player=="rock" and computer == 'paper':
    print("computer wins")
elif player =="rock" and computer =="scissors":
    print("player wins")
elif player =="paper" and computer =="rock":
    print("player wins")
elif player =="paper" and computer =="scissors":
    print("computer wins")
elif player == "scissors" and computer =="rock":
    print("computer wins")
elif player == "scissors" and  computer == "paper":
    print("player wins")

