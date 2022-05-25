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
        print(" XXXX INCORRECT XXXX\n"
              "Try again you can do it!")
