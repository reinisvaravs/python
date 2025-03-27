def main():
    a = int(input("Ievadiet a: "))
    b = int(input("Ievadiet b: "))

    print("\nx   y")
    print("-----")

    for x in range(a, b + 1):
        y = 3 * (2 * x + 7) # iedota vienādība
        print(f"{x}  {y}")

if __name__ == "__main__":
    main()
