#####  PROJECT 3  GUESSES NUMBER GAME  #######

import random

def guess_number():
  random_number = random.randint(1, 15)

  print("WELCOME TO THE NUMBER GUESSING GAME (User)!")
  print("I AM THINKING OF A NUMBER BETWEEN 1 TO 100.")
  
  while True:
    user_input = int(input("Enter Number: "))

    if user_input < random_number:
      print("Too Low")
    elif user_input > random_number:
      print("Too High")
      continue
    else:
      print("Correct Number:", random_number)
      break

if __name__ == "__main__":
  guess_number()