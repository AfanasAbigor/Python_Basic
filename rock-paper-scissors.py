import random

#Seed = int(input("Enter Any random seed Number:"))
#random.seed(Seed)

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

you = int(input("What Do you Choose? Type 0 for Rock, 1 for paper or 2 for Scissors: "))

yt = str(you)

if you == 0:
    print(rock)
elif you == 1:
    print(paper)
else:
    print(scissors)

print("Computer Chose:")

pc = random.randint(0,2)
pt = str(pc)
if pc == 0:
    print(rock)
elif pc == 1:
    print(paper)
else:
    print(scissors)

if(yt=="0" and pt=="2"):
    print("You Win.")
elif(yt=="2" and pt=="0"):
    print("You Loss.")
elif(yt=="2" and pt=="1"):
    print("You Win.")
elif(yt=="1" and pt=="2"):
    print("You Loss.")
elif(yt=="1" and pt=="0"):
    print("You Win.")
elif(yt=="0" and pt=="1"):
    print("You Loss.")
else:
    print("It's A draw.")
