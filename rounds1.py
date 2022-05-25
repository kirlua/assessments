
rounds_playing = int(input("How many rounds do you want to play?(must be and "   " integer between 1 and 10):"))
#Keep asking until a valid amount (1-10) is entered
while not 1 <= rounds_playing <= 10:
    print("Try again. Please enter a whole number between 1 and 10: ")

print(f" You are playing  {rounds_playing} times enjoy!")
