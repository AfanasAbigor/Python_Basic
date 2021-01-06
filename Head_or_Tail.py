import random

se_ed = int(input("Enter Any Seed Number: "))
random.seed(se_ed)

print("Let's toss, see what you got!!!")
decision = str(input("Do you want to proceed. press Y/N: ").lower())

if decision == "y":
    ran_num = random.randint(0, 1)

    if ran_num == 1:
        print("Heads.")
    elif ran_num == 0:
        print("Tails.")
elif decision == "n":
    print("You Have no Guts to check your Luck.")
