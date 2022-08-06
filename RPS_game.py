# Welcome to a simple rock, paper and scissors game.
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to the rock, paper and scissors game")
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if (user == 0):
 print(f"{rock}")
elif(user == 1):
  print(f"{paper}")
elif(user == 2):
  print(f"{scissors}")
else:
  print("incorrect input")

computer = int(random.randint(0,2))
print(f"Computer choose {computer}")
if (computer == 0):
 print(f"{rock}")
elif(computer == 1):
  print(f"{paper}")
elif(computer == 2):
  print(f"{scissors}")
else:
  print("incorrect input")

if (user == computer):
  print("Its a draw")
elif(user == 0 and computer == 2):
  print("You won")
elif(user == 1 and computer == 0):
  print("You won")
elif(user == 2 and computer == 1):
  print("You won")
else:
  print("Computer won")
  