import random

def print_result(count: int):
    odd_count = 0
    two_digit_sum = 0
    two_digit_count = 0
    one_digit_product = 1
    one_digit_found = False
    max_number = None

    for i in range(1, count + 1):
        num = random.randint(-15, 15)
        print(f"{i}: {num}")

        # Count odd numbers
        if num % 2 != 0:
            odd_count += 1

        # Handle two-digit numbers
        if 10 <= abs(num) <= 99:
            two_digit_sum += num
            two_digit_count += 1

        # Handle one-digit numbers (excluding 0)
        if 1 <= abs(num) < 10:
            one_digit_product *= num
            one_digit_found = True

        # Track max
        if max_number is None or num > max_number:
            max_number = num

    # Output results
    print(f"\nNepāra skaitļu skaits : {odd_count}")

    if two_digit_count > 0:
        avg = two_digit_sum / two_digit_count
        print(f"Divciparu skaitļu vidējā vērtība : {avg:.2f}")
    else:
        print("Divciparu skaitļu nav")

    if one_digit_found:
        print(f"Vienciparu skaitļu reizinājums : {one_digit_product}")
    else:
        print("Vienciparu skaitļu nav")

    if count > 0:
        print(f"Vislielākais skaitlis : {max_number}")

def main():
    count = int(input("Ievadiet skaitļu skaitu: "))
    print_result(count)

if __name__ == "__main__":
    main()
