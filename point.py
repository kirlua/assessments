import random
score = 0
name = input("What is your name?:")
print("Hello", name)
print()
print()
print("Welcome to Maori language Quiz")
print("Each question worth a point if you get 1 question wrong it -1 your point")
print(" Your current score is", score)

answer = input("What is Monday in Maori?:")
if answer == "Rahina":
    print("That is the correct answer")
    score = score + 1
    print("Your current score is", score)
else:
    print("that is incorrect")
    score = score - 1
    print("Your current score is", score)



