import random
#This uses two ordinary (1-dimensional) lists

print("This is a Maori quiz program. It asks you months and days of the week in Maori.\n"
      "You will have to type months and days of the week correctly in Maori.\n")
""" Ask user how many rounds they want to play with and check that the input is a valid integer
between 1 and 10. If it is, this amount becomes the balance in their account"""

user_balance = int(input("How many rounds do you want to play?(must be and "   " integer between 1 and 10):"))
#Keep asking until a valid amount (1-10) is entered
while not 1 <= user_balance <= 10:
    print("Try again. Please enter a whole number between 1 and 10: ")

print(f" You are playing  {user_balance} times enjoy!")

# 1st list
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# 2nd list
days_of_the_week_Maori = ["Rahina", "Ratu", "Raapa", "Rapare", "Ramere", "Rahoroi", "Ratapu"]
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


