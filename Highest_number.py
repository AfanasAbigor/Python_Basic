list = input("Enter Numbers: ").split()

"""
print(max(list))
print(min(list))

"""

n = int(len(list))

temp = 0
for i in range (0,n):
    list[i] = int(list[i])
    if list[i]>=temp:
        temp = list[i]

print(temp)

"""
list = input("Enter Numbers: ").split()
temp = 0;

for i in list:
    tempo = int(i)
    if tempo>=temp:
        temp = tempo
print(temp)
"""
