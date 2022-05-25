"""Component 3 (rounds) V3
More efficient method - includes valid range as the basis of the while loop
 which eliminates the need to use the valid variable"""

#Main routine
error = "That was not valid input\n"
user_balance = 0

# Keep asking until a valid amount (1-10) is entered
while not 1 <= user_balance <= 10:
    try:
        # ask for amount
        user_balance = int(input("Please enter a whole number between 1 and 10 to play this game\n"
                                 "how many rounds are you planning to play? :"))

        print()

    except ValueError:
        print(error)

print(f"You are playing {user_balance} rounds enjoy!")

