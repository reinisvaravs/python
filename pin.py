def main():
    correct_pin = "1654"
    attempts = 3

    while attempts > 0:
        entered_pin = input("Ievadiet PIN kodu: ")
        if entered_pin == correct_pin:
            print("\n" + "=" * 38)
            print("             Bankas ATM")
            print("=" * 38)
            print("        Jūsu konta atlikums")
            print("-" * 38)
            print("       Konta Nr.: 123-456-789")
            print("       Atlikums: 3250.75 eur")
            print("-" * 38)
            return
        else:
            print("Nepareizs PIN kods.")
            attempts -= 1

    print("Piekļuve liegta. Mēģinājumu skaits pārsniegts.")

if __name__ == "__main__":
    main()
