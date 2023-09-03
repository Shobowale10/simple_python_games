import random

guess = input("Type a number to start the game: ")

if guess.isdigit():

    guess = int(guess)
    if guess <= 0:
        print("Please print a number greater than 0 next time")    
        quit()
else:
    print("You did'nt enter a number.")
    quit()


random_number = random.randint(0, 10)
guesses = 0

while guess != random_number:
    guesses += 1
    user_guess = input("Guess a number: ")

    if user_guess.isdigit():
            user_guess = int(user_guess)
    else:
            print("You did'nt enter a number.")
            continue

    if user_guess == random_number:
            print("Correct!")
            if guesses < 5:
                print("You got it right after" ,guesses,"guesses. You're brilliant.")
            else:
                print("You got it right after" ,guesses,"guesses. You're not brilliant.")
            break
    elif user_guess > random_number:
            print("You were above the number!")
    else:
            print("You were below the number!")
            continue
    

 