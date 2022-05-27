# variables needed
instruction = " Sunday is Ratapu Monday is Rahina Tuesday is Ratu Wednesday is Raapa " \
              "Thursday is Rapare Friday is Ramere Saturday is Rahori 1 is tahi 2 is rua 3 is toru 4 is wha 5 is rima 6 is ono 7 is whitu 8 is waru 9 is iwa 10 is tekau"
"instructions"
show_instruction = input("Have you played this game before?: ")

# if player say yes dont show instruction
if show_instruction == "yes":
    print("program continue")
elif show_instruction == "no":
    print("show instructions")
    print(instruction)
