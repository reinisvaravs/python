import random

while True:
    ran_number = random.randint(1, 2)
    attempt = 0

    while True:
        try:
            user_input = int(input("Guess the number between 1 and 100: "))
            if user_input > ran_number:
                print("Too high!")
                attempt += 1
            elif user_input < ran_number:
                print("Too low!")
                attempt += 1
            elif attempt == 0 and user_input == ran_number:
                print("You guessed it in one!")
                break
            else:
                print(f"Congrats! You guessed the number in {attempt + 1} attempts!")
                break
        except ValueError:
            print("Please enter a valid number!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
