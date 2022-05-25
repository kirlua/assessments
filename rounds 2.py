""" Component 2 (Rounds) v2
Use try/accept and pull error message out of the loop """

error = "Please enter a whole number between 1 and 10 to play the game\n"
valid = False

#Keep asking until a valid amount (1-10) is entered
while not valid:
    try:
        # ask for amount
        user_balance = int(input("How many rounds would you like to play? :"))

        # check if the amount is too high/low
        if 0< user_balance <= 10:
            print(f"You are playing {user_balance} times")
            valid = True
        else:
            print(error)

    except ValueError:
        print(error)
