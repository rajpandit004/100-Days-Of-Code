# PROJECT: ROCK PAPER SCISSORS

import random

print("Welcom to the Rock Paper Scissors Game!")
print("[A] The outcome of the game is determined by 3 simple rules:")
print("\t1. \"Rock\" wins against \"Scissors\"")
print("\t2. \"Scissors\" wins against \"Paper\"")
print("\t3. \"Paper\" wins against \"Rock\"")
print("[B] You have to Type \"0\" for Rock, \"1\" for Paper and \"2\" for Scissors")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("\nWhat do you choose?\n"))

if user_choice > 2 or user_choice < 0:
    print()
    print("You Entered Invalid Choice. Game Over!")
else:
    print()
    image = [rock, paper, scissors]

    computer_choice = random.randint(0, 2)

    # Deciding winner based on choice
    if user_choice == 0 and computer_choice == 2:
        print(f"Your's Choice:\n{image[user_choice]}")
        print(f"Computer's Choice:\n{image[computer_choice]}")
        print("You Won!")
    elif user_choice == 2 and computer_choice == 0:
        print(f"Your's Choice:\n{image[user_choice]}")
        print(f"Computer's Choice:\n{image[computer_choice]}")
        print("You Lose!")
    elif user_choice > computer_choice:
        print(f"Your's Choice:\n{image[user_choice]}")
        print(f"Computer's Choice:\n{image[computer_choice]}")
        print("You Won!")
    elif user_choice < computer_choice:
        print(f"Your's Choice:\n{image[user_choice]}")
        print(f"Computer's Choice:\n{image[computer_choice]}")
        print("You Lose!")
    elif user_choice == computer_choice:
        print(f"Your's Choice:\n{image[user_choice]}")
        print(f"Computer's Choice:\n{image[computer_choice]}")
        print("It's a Draw!")

    print("\n\tTHANK YOU FOR PLAYING!")
