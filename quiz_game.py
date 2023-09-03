play = input("Do you want to play a quiz game? ")
if play != "yes":
    quit()
print("Okay, Let's play :)")


score = 0
question = input("What is the name of the game we're playing?")
if question.lower() == "quiz game":
    score += 1
    print("Correct")
else:
    print("Incorect")


question = input("What is the name of the institute we're in?")
if question.lower() == "globaltech":
    score += 1
    print("Correct")
else:
    print("Incorect")


question = input("What programming language are we using? ")
if question.lower() == "python":
    score += 1
    print("Correct")
else:
    print("Incorect")


question = input("What is the full meaning of CPU? ")
if question.lower() == "central processing unit":
    score += 1
    print("Correct")
else:
    print("Incorect")


question = input("What is the full meaning of HTML? ")
if question.lower() == "hypertext markup language":
    score += 1
    print("Correct")
else:
    print("Incorect")
    

if score < 5:
    print("Olodo, Your scrore is", score, "out of 5.")
else:
    print("Brilliant, Your scrore is", score, "out of 5.")
