sp=15
mp=20
lp=25
price = 0

size = str(input("What Size of Pizza you Want? S, M, or L: "))
if size == "S":
    price = sp
elif size == "M":
    price = mp
elif size == "L":
    price = lp
pepperoni = str(input("Do you wants pepperoni? Y/N:"))
if pepperoni == "Y":
    if price == 15:
        price += 2
    else:
        price += 3
extra_chess = str(input("Do you wants Extra Chess? Y/N:"))
if extra_chess == "Y":
    price += 1

print(f"Your Final Bill is {price}.")
