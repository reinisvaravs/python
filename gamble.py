import random

def main():
    credits = 100
    print(f"Jūsu kredīti: {credits}")

    while credits >= 20:
        choice = input("Vai vēlies griezt (20 kredīti)? (y/n): ").lower()
        if choice != "y":
            break

        credits -= 20
        spin = [random.randint(1, 7) for _ in range(3)]
        print(*spin, end=" => ")

        if spin[0] == spin[1] == spin[2]:
            print("Laimests: 100")
            credits += 100
        elif spin[0] == spin[1] or spin[1] == spin[2] or spin[0] == spin[2]:
            print("Laimests: 30")
            credits += 30
        else:
            print("Laimests: 0")

        print(f"Jūsu kredīti: {credits}")

    if credits < 20:
        print("\nJums pietrūkst kredīti, lai turpinātu spēli!")

if __name__ == "__main__":
    main()
