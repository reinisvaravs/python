def main():
    count = int(input("Ievadiet pirmo pirmskaitļu skaitu: "))
    found = 0
    num = 2

    while found < count:
        if is_prime_number(num):
            print(num)
            found += 1
        num += 1
        
        
def is_prime_number(x: int) -> bool:
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True



if __name__ == "__main__":
    main()
