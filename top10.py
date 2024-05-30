# ------- FUNCTIONS -----------
def intro():
    name = input("What's your name?")
    print("Welcome to this quiz,", name)
    print("This quiz is about the top ten dictators with the highest kill count in history")

def getLives():
    while True:
        lives = int(lives)
        try:
            if lives >= 0:
                return lives
            else:
                print("Please choose a positive number")
        except:
            print("That wasn't a number")

lives = getLives()

DICTATORS_WITH_THE_HIGHEST_KILL_COUNT_ANSWERS = ["Mao Zedong", "Joseph Stalin", "Adolf Hitler", "Leopold II of Belgium", "Hideki Tojo", "Ismail Enver Pasha", "Pol Pot", "Kim Il Sung", "Mengistu Haile Mariam", "Yakubu Gowon"]
            
def isCorrect(answer, list):
    if answer in list:
        return True
    else:
        return False

score = 0   
while lives > 0:
    answer = input("Name one of the top ten dictators with the highest kill count in history")

if isCorrect(answer, DICTATORS_WITH_THE_HIGHEST_KILL_COUNT_ANSWERS) == True:
    print("Correct")
    score += 1
else:
    print("Wrong")
    lives -= 1

print("Game over. Your final score was {}".format(score))


# --------- MAIN CODE ----------
intro()

