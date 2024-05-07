#import random
#print(random.randint(0, 11))

score = 0

# Ask the user their name and save it
name = input("Hello, what's your name?")

# Greet the user and introduce the quiz
print("Welcome to the science quiz",name)

# Ask the user a question
answer = input("Q.1 What is Carbon's atomic number?")

# Check the user’s answer and give feedback
if answer == "6":
    print("Correct!")
    score += 1
elif answer == "":
    print("Not sure?")
else:
    print("Wrong!")
    print("The answer is 6")

answer = input("Q.2 True or False the element Argon is a noble gas")
answer = answer.lower()

if answer == "true":
    print("Correct!")
    score += 1 
elif answer == "false":
    print("Incorrect!")
elif answer == "":
    print("Not sure?")

answer = input("Q.3 What is the name of the 12th element on the periodic table?")
answer = answer.lower()

if answer == "magnesium":
    print("Correct!")
    score += 1
elif answer == "":
    print("Not sure?")
else:
    print("Wrong!")
    print("The answer is Magnesium")

answer = input("Q.4 What element does the symbol Au on the periodic table represent?")
answer = answer.lower()

if answer == "gold":
    print("Correct!")
    score += 1
elif answer == "":
    print("Not sure?")
else:
    print("Wrong!")
    print("The answer is Gold")

answer = input("Q.5 True or False the letter Q is not used in the symbol of any element on the periodic table")
answer = answer.lower()

if answer == "true":
    print("Correct!")
    score += 1 
elif answer == "false":
    print("Incorrect!")
elif answer == "":
    print("Not sure?")

question = "Q.6 What element does the symbol Ni represent?"
a = "Nitrogen"
b = "Nickel"
c = "Nihonium"
d = "Niobium"
answer = input("{}\nA.{} B.{} C.{} D.{}".format(question, a, b, c, d)).lower()

if answer == b or answer == "b":
    print("Correct!")
    score += 1
elif answer == "":
    print("Not sure?")
elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d"
    print("That wasn't an option")

# End the quiz
if score < 9:
    print("It's now the end of the quiz {}, you got {} out of 10 questions correct, thanks for playing.".format(name, score))
else:
    print("It's now the end of the quiz {}, congratulations on getting all the questions correct, you did great, thanks for playing.".format(name))
