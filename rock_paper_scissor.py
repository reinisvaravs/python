import random

emojis = { "r": "🪨", "s": "✂️", "p": "📃" }
choices = ("r", "p", "s")

user_score = 0
computer_score = 0

def score():
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print("")

while True:
    user_choice = input("Rock, paper or scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid choice!") 
        continue

    computer_choice = random.choice(choices)

    print("")
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")
    print("")

    if user_choice == computer_choice:
        print(">> Tie")
        score()
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "r")):
        print(">> You win")
        user_score = user_score + 1
        score()
    else:
        print(">> You lose!")
        computer_score = computer_score + 1
        score()

    should_continue = input("Continue? (y/n): ").lower()
    if not should_continue == "y":
        break