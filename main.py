import random
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
---'   ____)____
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

#Write your code below this line 👇


your_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
icon_user = ''
icon_computer = ''
converted_choice_int = int(your_choice)
computer_choice = random.randint(0,2)
print(f"Your choice: {converted_choice_int}")
if converted_choice_int == 0:
  print(rock)
elif converted_choice_int == 1:
  print(paper)
elif converted_choice_int == 2:
  print(scissors)
else:
  print("Your choice doesn't exist")


print(f"Computer's choice: {computer_choice}")
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print(scissors)
else:
  print("Your choice doesn't exist")

if converted_choice_int == computer_choice:
  print("Draw")
elif (converted_choice_int == 0 and computer_choice == 2) or (converted_choice_int == 1 and computer_choice == 0) or (converted_choice_int == 2 and computer_choice == 1):
  print("You WON!")
else:
  print("Computer WON!")