import random

print(r'''
 __      __   _                    _____      ___         _     ___                      ___     _                      ___                
 \ \    / /__| |__ ___ _ __  ___  |_   _|__  | _ \___  __| |__ | _ \__ _ _ __  ___ _ _  / __| __(_)______ ___ _ _ ___  / __|__ _ _ __  ___ 
  \ \/\/ / -_) / _/ _ \ '  \/ -_)   | |/ _ \ |   / _ \/ _| / / |  _/ _` | '_ \/ -_) '_| \__ \/ _| (_-<_-</ _ \ '_(_-< | (_ / _` | '  \/ -_)
   \_/\_/\___|_\__\___/_|_|_\___|   |_|\___/ |_|_\___/\__|_\_\ |_| \__,_| .__/\___|_|   |___/\__|_/__/__/\___/_| /__/  \___\__,_|_|_|_\___|
                                                                        |_|                                                                
''')

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