
import random
score = 0


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

    # 1st list
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "1", "2", "3", "4", "5","6", "7", "8", "9", "10"]
    # 2nd list
    days_of_the_week_Maori = ["Rahina", "Ratu", "Raapa", "Rapare", "Ramere", "Rahoroi", "Ratapu", "tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
    question = random.choice(days_of_the_week)
    print(question)

    # Using the index position of the question in one list to find the corresponding
    # Index position of the answer

    answer_index = days_of_the_week.index(question)
    answer = days_of_the_week_Maori[answer_index]

    # Compare the attempt to see if it matches the correct answer
    attempt = input(f" what is {question} in Maori: ")

    if attempt == answer:
        print("#### CORRECT ####\n"
              "Let's go to the next question")
    else:
        print(" XXXX INCORRECT XXXX\n")
