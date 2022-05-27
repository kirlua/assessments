import random
score = 0

 # yes/no checking function
def yes_no(question_text):
    while True:
        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Program Continues'
        if answer == "yes" or answer == "y" :
            answer = "Yes"
            return "yes"


        # If they say no, output 'Display instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return "no"

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no' ")

 #variables needed
instruction = " Sunday is Ratapu Monday is Rahina Tuesday is Ratu Wednesday is Raapa Thursday is Rapare Friday is Ramere Saturday is Rahori 1 is tahi 2 is rua 3 is toru 4 is wha 5 is rima 6 is ono 7 is whitu 8 is waru 9 is iwa 10 is tekau"
"instructions"
show_instruction = yes_no("Have you played this game before?:")
if show_instruction == "no":
    print(instruction)

    # loop until player get it right


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
        print("That is the correct answer")
        score = score + 1
        print("Your current score is", score)
        print("Great work!")
    else:
        print(" XXXX INCORRECT XXXX\n")
        print("that is incorrect")
        score = score - 1
        print("Your current score is", score)
        print(" Very close one!")









