import random



error = "Please enter a whole number between 1 and 10 to play the game\n"
valid = False

#Keep asking until a valid amount (1-10) is entered
while not valid:
    try:
        # ask for amount
        rounds_playing = int(input("How many rounds would you like to play? :"))

        # check if the amount is too high/low
        if 0< rounds_playing <= 10:
            print(f"You are playing {rounds_playing} times")
            valid = True
        else:
            print(error)

    except ValueError:
        print(error)

round = 0
while round < rounds_playing:

    round += 1

num1 = random.randint(1,9)

answer = the answer was ()


answer =
    if answer == user_input
        print("Correct well done!")
    else:
        print(f"Very close. The answer was {user_input}")
