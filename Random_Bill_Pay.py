import random

Seed = int(input("Enter Any Seed Number: "))
random.seed(Seed)

name_list = str(input("Enter Names Using comma ',' and Spaces ' '  : ")) # input names

name = name_list.split(", ") # splitting "," and " " from list and make it list

length = int(len(name) - 1) # length of the list

ranDom = random.randint(0,length) 

person = name[ranDom]

print(f"{person} is Going to Buy the meal today.")
