import random

def main():
    secret = random.randint(1, 99)
    tries = 0

    print("Uzmini skaitli no 1 līdz 99 !!!")
    while True:
        guess = int(input("Ievadi skaitli: "))
        tries += 1

        if guess < secret:
            print("Nē, iedomātais skaitlis ir lielāks")
        elif guess > secret:
            print("Nē, iedomātais skaitlis ir mazāks")
        else:
            print(f"\nApsveicam! Tu atminēji skaitli {secret} ar {tries}. reizi")
            break

if __name__ == "__main__":
    main()
