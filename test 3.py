import random
#This uses two ordinary (1-dimensional) lists

print("This is a Maori quiz program. It asks you numbers and days of the week in Maori.\n"
      "You will have to type months and days of the week correctly in Maori.\n")
""" Ask user how many rounds they want to play with and check that the input is a valid integer
between 1 and 10. If it is, this amount becomes the balance in their account"""

list and print("Sunday is Ratapu", "Monday is Rahina", "Tuesday is Ratu", "Wednesday is Raapa", "Thursday is Rapare", "Friday is Ramere", "Satudrday is Rahori")
list and print("1 is tahi", "2 is rua", "3 is toru", "4 is wha", "5 is rima", "6 is ono", "7 is whitu", "8 is waru", "9 is iwa", "10 is tekau")
"""Took function from component 03_v1 as the basis for this new function which incorporates both yes/no and show
instructions"""

# yes/no checking function
def yes_no(question_text):
    while True:
        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Program Continues'
        if answer == "yes" or answer == "y":
            answer = "yes"
            return answer

        # If they say no, output 'Display instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no' ")

# Main routine go here...
show_instructions = yes_no ("Have you played this game before? :")

print(f"You entered '{show_instructions}'")
# If it enters n or no show instructions
print(f" This game is about learning Maori language, it teaches you about the days of the week and numbers in Maori ")
print(f"")



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


# 1st list
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "1", "2", "3", "4", "5","6", "7", "8", "9", "10"]
# 2nd list
days_of_the_week_Maori = ["Rahina", "Ratu", "Raapa", "Rapare", "Ramere", "Rahoroi", "Ratapu", "tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
question = random.choice(days_of_the_week)
print(question)
attempt = input(f" what is {question} in Maori: ")

# Using the index position of the question in one list to find the corresponding
# Index position of the answer

answer_index = days_of_the_week.index(question)
answer = days_of_the_week_Maori[answer_index]

# Compare the attempt to see if it matches the correct answer
if attempt == answer:
    print("#### CORRECT ####\n"
          "Let's go to the next question")
else:
    print(" XXXX INCORRECT XXXX\n"
          "Try again you can do it!")




