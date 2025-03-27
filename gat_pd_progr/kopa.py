import math

def main():
    while True:
        num = float(input("Ievadi skaitli (0, lai beigtu): "))

        if num == 0:
            break
        if num < 0:
            continue

        print(f"Ievadītā skaitļa kvadrātsakne ir: {math.sqrt(num):.2f}")

if __name__ == "__main__":
    main()
