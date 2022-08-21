random_number = 10
guess = 0

while guess != random_number
      guess = int(input("Guess a number between 1 and 10:"))
  
      if guess < random_number:
         print("Sorry, Try again. Too Low")
    elif guess > random_number:
           print("Sorry, Try again. Too high")
      else:
           print("Congratulations, you have guessed the correct number")
