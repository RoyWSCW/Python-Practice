#import random
#print(random.randint(0, 11))

score = 0
QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{}\n"

# Ask the user their name and save it
name = input("Hello, what's your name?\n")

# Greet the user and introduce the quiz
print("Welcome to the science quiz",name)

# Ask the user a question
answer = input("Q.1 What is Carbon's atomic number?\n")

# Check the user’s answer and give feedback
if answer == "6" or answer == " 6":
    print("Correct!")
    score += 1
elif answer == "":
    print("Not sure?")
else:
    print("Wrong!")
    print("The answer is 6")

answer = input("Q.2 True or False the element Argon is a noble gas\n")
answer = answer.lower()

if answer == "true" or answer == " true" or answer == "t" or answer == " t":
    print("Correct!")
    score += 1 
elif answer == "false" or answer == " false" or answer == "f" or answer == " f":
    print("Incorrect!")
elif answer == "":
    print("Not sure?")

answer = input("Q.3 What is the name of the 12th element on the periodic table?\n")
answer = answer.lower()

if answer == "magnesium" or answer == "mg":
    print("Correct!")
    score += 1
elif answer == "":
    print("Not sure?")
else:
    print("Wrong!")
    print("The answer is Magnesium")

answer = input("Q.4 What element does the symbol Au on the periodic table represent?\n")
answer = answer.lower()

if answer == "gold" or answer == " gold":
    print("Correct!")
    score += 1
elif answer == "":
    print("Not sure?")
else:
    print("Wrong!")
    print("The answer is Gold")

answer = input("Q.5 True or False the letter Q is not used in the symbol of any element on the periodic table\n")
answer = answer.lower()

if answer == "true" or answer == " true" or answer == "t" or answer == " t":
    print("Correct!")
    score += 1 
elif answer == "false" or answer == " false" or answer == "f" or answer == " f":
    print("Incorrect!")
elif answer == "":
    print("Not sure?")

question = "Q.6 What element does the symbol Ni represent?"
a = "Nitrogen"
b = "Nickel"
c = "Nihonium"
d = "Niobium"
answer = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()

if answer == b.lower() or answer == "b":
    print("Correct!")
    score += 1
elif answer == "":
    print("Not sure?")
elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
    print("That wasn't an option")
else:
    print("Wrong!")
    print("The answer is Nickel")

answer = input("Q.7 What is sodium's symbol on the periodic table?\n")
answer = answer.lower()

if answer == "na" or answer == " na":
    print("Correct!")
    score += 1
elif answer == "":
    print("Not sure?")
else:
    print("Incorrect!")
    print("The answer is Na")

question = "Q.8 How many elements are on the periodic table?"
a = "117"
b = "118"
c = "119"
d = "120"
answer = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()

if answer == b or answer == "b" or answer == " 118" or answer == "118":
    print("Correct!")
    score += 1
elif answer == "":
    print("Not sure?")
elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
    print("That wasn't an option")
else:
    print("Wrong!")
    print("The answer is 118")

answer = input("Q.9 True or False the letter J is not used in the symbol of any element on the periodic table\n")
answer = answer.lower()

if answer == "true" or answer == " true" or answer == "t" or answer == " t":
    print("Correct!")
    score += 1 
elif answer == "false" or answer == " false" or answer == "f" or answer == " f":
    print("Incorrect!")
elif answer == "":
    print("Not sure?")

question = "Q.10 Is the person who made this quiz a better coder than you, for this specific question please only answer in one letter"
a = "yes"
b = "no, just kidding of course yes"
c = "yes because im a bad coder"
d = "Opposite of no (yes)"
answer = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()

if answer == a and answer == "a" and answer == b and answer == "b" and answer == c and answer == "c" and answer == d and answer == "d":
    print("Correct!")
    score += 1
elif answer == "":
    print("Not sure?")
elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
    print("That wasn't an option")
else:
    print("Wrong!")
    print("The answer is any of the above and you know it")

# End the quiz
if score < 9:
    print("It's now the end of the quiz {}, \nyou got {} out of 10 questions correct, thanks for playing.".format(name, score))
else:
    print("It's now the end of the quiz {}, \ncongratulations on getting all the questions correct, you did great, thanks for playing.".format(name))
