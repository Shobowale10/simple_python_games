import random

user_score = 0
computer_score = 0
user_wins = 0
computer_wins = 0


options = ["rock","paper","scissors"]
while True:
    user_input = input("Pick an option in rock,paper,scissors to play or q to quit: ").lower()

    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
            print("You won!")
            user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
            print("You won!")
            user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
            print("You won!")
            user_wins += 1
    else:
            print("Compuer Wins!")
            computer_wins += 1

if (user_wins > computer_wins):
        winner = "You Won !!"
else:
        winner = "Computer Won!!"

print("You won", user_wins, "times.")
print("The Computer won", computer_wins, "times.")
print(winner)
print("Goodbye!")