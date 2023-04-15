#imports the libraries
import random
import math


#introduction to game
print("""hello!!!
this is a guessing game.
please enter your bound for the game to start""")


#gets user inputs for upper and lower boundaries
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

#generates random number in chosen boundaries
x = random.randint(lower, upper)
print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")

#sets number of guesses to 0 creating a counter
guess_count = 0

#while loop for the rounds of the game
while guess_count < math.log(upper - lower + 1, 2):
    guess_count += 1

    #takes the guessed number as an input
    guess = int(input("Guess a number:- "))

    #testing if the guessed number is the correct one
    if x == guess:
        print("Congratulations you did it in ",
              guess_count, " try")
        #if number is guessed loop will break
        break
    elif x > guess:
        print("You guessed too small!")
        print("You have ", round(math.log(upper - lower + 1, 2)) -
              guess_count, " guess left")
    elif x < guess:
        print("You Guessed too high!")
        print("You have ", round(math.log(upper - lower + 1, 2)) -
              guess_count, " guess left")


#if number has been gussed more times than there is chances the game ends
if guess_count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
