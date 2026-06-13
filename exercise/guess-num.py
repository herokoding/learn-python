# initialize the number of guesses made so far
trying = 0
# the secret number to guess
answer = 8
# maximum allowed guesses before the game ends
limit = 3

while trying < limit:
    # prompt the player for their guess
    guess = int(input("Enter your guess: "))
    trying += 1
    
    # check whether the guess is correct or provide a hint
    if guess == answer:
        print("Congratulations! You guessed the number in " + str(trying) + " tries!")
        break
    elif guess < answer:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
        break
    
# this extra increment is outside the loop and will always run once
trying += 1