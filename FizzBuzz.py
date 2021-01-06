#Fizz buzzz
#num%3 fizz, num%5 buzz, num%both fizzBuzz

n = int(input("Enter Range: "))

for i in range(1,n+1):
  if i%3==0 and i%5==0:
    print("FizzBuzz")
  elif i%3==0:
    print("Fizz")
  elif i%5==0:
    print("Buzz")
  else:
    print(i)
