import random
n = random.randint(1,10)
guesses = 1
a = input("Enter a number: ")
while(guesses != 3):
    if(a == n):
      print("Correct")
      print("Your guesses: ", guesses)
      break
    elif(a < n):
      a = 0
      guesses += 1
      print("Too low! Guess again")
      a = input("Enter a number: ")
      print("Your guesses: ", guesses)
    elif(a > n):
      a = 0
      guesses += 1
      print("Too High! Guess again")
      a = input("Enter a number: ")
      print("Your guesses: ", guesses)