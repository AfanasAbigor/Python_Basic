height = int(input("Enter Your Height: "))
if height >= 120:
    print("You Can Ride.")

    age = int(input("Enter Your Age: "))
    bill = 0
    if age>18:
        if age>=45 and age<=55:
            bill=0
            print("Every Thing gonna be Ok, Have a free drive on us.")
        else:
            bill=12
            print("You have to Pay $12.")

    elif age<=18:
        if age<12:
            print("You Have To Pay $5")
            bill = 5
        else:
            print("You Have To Pay $7")
            bill = 7
    photo = str(input("Do You Wants To Take a Picture? Y/N: "))
    if photo == "Y":
        bill += 3
    print(f"Your Final Bill is {bill}.\nThank You.")

else:
    print("You Can Not Ride")
