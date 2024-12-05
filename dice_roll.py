import random

roll_array = []
last_roll = None
streak_count = 0

while True:
    choice = input("Roll the dice? (y/n): ").lower()

    if choice == "y":
        die = random.randint(1, 6)
        print(f"You rolled: {die}")
        roll_array.append(die)

        # Check for a streak
        if die == last_roll:
            streak_count += 1
            if streak_count >= 1:
                print(f"Streak! {die} has been rolled {streak_count + 1} times in a row!")
        else:
            streak_count = 0 

        last_roll = die
    elif choice == "n":
        print("Thank you for playing!")
        break
    else:
        print("Invalid input!")