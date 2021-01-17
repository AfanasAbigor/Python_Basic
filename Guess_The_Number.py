logo = """

   ▄██████▄  ███    █▄     ▄████████    ▄████████    ▄████████     ███        ▄█    █▄       ▄████████ 
  ███    ███ ███    ███   ███    ███   ███    ███   ███    ███ ▀█████████▄   ███    ███     ███    ███ 
  ███    █▀  ███    ███   ███    █▀    ███    █▀    ███    █▀     ▀███▀▀██   ███    ███     ███    █▀  
 ▄███        ███    ███  ▄███▄▄▄       ███          ███            ███   ▀  ▄███▄▄▄▄███▄▄  ▄███▄▄▄     
▀▀███ ████▄  ███    ███ ▀▀███▀▀▀     ▀███████████ ▀███████████     ███     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     
  ███    ███ ███    ███   ███    █▄           ███          ███     ███       ███    ███     ███    █▄  
  ███    ███ ███    ███   ███    ███    ▄█    ███    ▄█    ███     ███       ███    ███     ███    ███ 
  ████████▀  ████████▀    ██████████  ▄████████▀   ▄████████▀     ▄████▀     ███    █▀      ██████████ 
                                                                                                       
███▄▄▄▄   ███    █▄    ▄▄▄▄███▄▄▄▄   ▀█████████▄     ▄████████    ▄████████                            
███▀▀▀██▄ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███   ███    ███                            
███   ███ ███    ███ ███   ███   ███   ███    ███   ███    █▀    ███    ███                            
███   ███ ███    ███ ███   ███   ███  ▄███▄▄▄██▀   ▄███▄▄▄      ▄███▄▄▄▄██▀                            
███   ███ ███    ███ ███   ███   ███ ▀▀███▀▀▀██▄  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀                              
███   ███ ███    ███ ███   ███   ███   ███    ██▄   ███    █▄  ▀███████████                            
███   ███ ███    ███ ███   ███   ███   ███    ███   ███    ███   ███    ███                            
 ▀█   █▀  ████████▀   ▀█   ███   █▀  ▄█████████▀    ██████████   ███    ███                            
                                                                 ███    ███                            
                                                                           Manas Sharma.
"""
print(logo)
print("Welcome to the Number Guessing Game!\nThink a number between 1 and 100")
import random

number = random.randint(1,100)

decision = input("Choose a difficulty. Type 'Easy' or 'Hard': ").lower()
#print(f"random number is {number}")

is_right = False
hard = 5
easy = 10
result = False # if false loss or true win
if decision == "easy":

    while is_right is False and easy!=0:
        print(f"You Have {easy} attempts remaining to guess the Number: ")
        guess = int(input("Make A Guess: "))
        if guess == number:
            print("Correct Guess.")
            is_right = True
            result = True
        elif guess < number:
            print("Too Low.")
        elif guess > number:
            print("Too High.")
        easy-=1

elif decision == "hard":

    while is_right is False and hard!=0:
        print(f"You Have {hard} attempts remaining to guess the Number: ")
        guess = int(input("Make A Guess: "))
        if guess == number:
            print("Correct Guess.")
            is_right = True
            result = True
        elif guess < number:
            print("Too Low.")
        elif guess > number:
            print("Too High.")
        hard-=1

if result == False:
    print("Times Up. YOU LOSS -_-")
elif result == True:
    print("Correct Answer. YOU WIN !!!")
