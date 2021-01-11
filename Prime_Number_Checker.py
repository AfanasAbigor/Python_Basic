def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n>2:
        for i in range(2,n):
            if n%i == 0:
                return False
            else:
                return True


number = int(input("Enter The Number: "))

result = isPrime(number)

if result == True:
    print(f"{number} is a Prime Number")
elif result == False:
    print(f"{number} is Not a Prime Number")
