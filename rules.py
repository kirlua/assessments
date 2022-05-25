"""Took function from component 03_v1 as the basis for this new function which incorporates both yes/no and show
instructions"""

# yes/no checking function
def yes_no(question_text):
    while True:
        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Program Continues'
        if answer == "yes" or answer == "y" :
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
print(f" game is about learning Maori language, it teaches you about the days of the week and numbers in Maori ")
print(f"")
having_fun = yes_no("Are you having fun? ")
print(f"You entered '(Having_fun)'")

