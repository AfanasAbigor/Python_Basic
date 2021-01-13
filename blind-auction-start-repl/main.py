import art
print(art.logo)
print("Welcome to the secret auction program.")
from replit import clear

decision = True
price = 0
name = ""

while decision is True:

  person_name = str(input("What is Your Name: "))
  bid = int(input("What's Your bid: $"))

  T_name = person_name
  T_price = bid

  if T_price > price:
    price = T_price
    name  = T_name
  next_bidder = str(input("Are There any bidder? type 'yes' or 'no'\n").lower())

  if next_bidder == "no":
    decision = False
    clear()
  else:
    clear()

print(f"The winner is {name} with a bid of ${price}")



 