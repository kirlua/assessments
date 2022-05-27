
import random
score = 0
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
        if answer == "yes" or answer == "y" :
            answer = "Yes"
            return answer


        # If they say no, output 'Display instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no' ")

# Main routine go here...


shoshow_instructions = input("Have you played this game before?: ")
priprint(f"You entered '{show_instructions}'")
if show_instructions == "no" or "n":
    print("show instruction")
    print(" This game is about learning Maori language, it teaches you about the days of the week and numbers in Maori ")
# If it enters n or no show instructions
elif show_instructions == "yes" or "y":
    print("played before")
else:
    print("Please enter yes or no")
print(f"")
