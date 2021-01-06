import random

Seed = int(input("Enter Any Seed Number: "))
random.seed(Seed)

name_list = str(input("Enter Names Using comma ',' and Spaces ' '  : "))

name = name_list.split(", ")

person = random.choice(name)
print(f"{person} is Going To Buy the Meal Today.")
