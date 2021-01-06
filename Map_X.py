row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")

integer = int(input("Give A Integer Input Between 11 to 33: "))

n = int(integer / 10)  # 23 ---> 2
m = int(integer % 10)  # 23 ---> 3

map[m-1][n-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
