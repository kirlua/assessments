"""Component 4 (Rounds) v4
Changing v3 into a function
Also needed to change user_balance to the more generic variable name 'rounds_you_are_playing'
and to change the condition and position of the number comparison into the loop to make the function
recyclable"""

def num_check(question, low, high):
    error = "That was not valid input\n"
    "Please enter a number between {} and {}\n".format(low,high)

    # Keep asking until a valid amount (1-10) is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # check for number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

