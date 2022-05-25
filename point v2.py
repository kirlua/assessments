import random


def version2():
    correct = "wrong"
    # loop until player get it right
    score = 0
    name = input("What is your name?:")
    print("Hello", name)
    print()
    print()
    print("Welcome to Maori language Quiz")
    print("Each question worth a point if you get 1 question wrong it -1 your point")
    print(" Your current score is", score)
    while correct != "correct":
        answer = input("*****What is Monday in Maori?****:")
        if answer == "Rahina":
            print("That is the correct answer")
            score = + 1
            correct = "correct"
            print("Your current score is", score)
        else:
            print("that is incorrect XXXXX, please try again until you get the right answer! :)")
            score = - 1


version2()





