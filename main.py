
# Ask the user their name and save it
name = input("Hello, what's your name?")

# Greet the user and introduce the quiz
print("Welcome to the science quiz",name)

# Ask the user a question
answer = input("What is Carbon's atomic number?")

# Check the user’s answer and give feedback
if answer == "6":
    print("Correct!")
elif answer == "":
    print("Not sure?")
else:
    print("Wrong!")
print("The answer is 6")
    
# End the quiz
print("It's now the end of the quiz, thanks for playing.")
