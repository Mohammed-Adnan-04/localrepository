import random
choices = ["rock","papper","sissor"]
computer_choice = random.choice(choices)
user_choice = str(input("enter your choice: "))
if user_choice == computer_choice:
    print("its draw")
elif user_choice=="rock" and computer_choice=="sissor":
    print(f"you win {user_choice} beats {computer_choice}")
elif user_choice=="sissor" and computer_choice=="rock":
    print(f"you lose {computer_choice} beats {user_choice}")
elif user_choice=="papper" and computer_choice == "rock":
    print(f"you win {user_choice} beats {computer_choice}")
