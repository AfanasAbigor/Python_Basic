name1 = str(input("Enter Your Name: "))
name2 = str(input("Enter His/Her Name: "))
final = str(name1+name2).lower()            #lower() for turn upper case into lower case.

cnt1 = final.count('t')
cnt2 = final.count('r')
cnt3 = final.count('u')
cnt4 = final.count('e')

true = int(cnt1+cnt2+cnt3+cnt4)


cnt5 = final.count('l')
cnt6 = final.count('o')
cnt7 = final.count('v')

love = int(cnt5+cnt6+cnt7+cnt4)

percentage = int(f"{true}{love}")

if percentage < 10 or percentage > 90:
    print(f"Your score is {percentage}, you go together like coke and mentos.")

elif percentage >= 40 and percentage <= 50:
    print(f"Your score is {percentage}, you are alright together")

else:
    print(f"Your score is {percentage}.")
