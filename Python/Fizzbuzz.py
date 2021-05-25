a = 5
b = 8
c = 15
for x in range(1, 101):
  if(x % c == 0):
    print("FizzBuzz")
  elif(x % a == 0):
    print("Fizz")
  elif(x % b == 0):
    print("Buzz")
  else:
    print(x)