def print_result():
    for num in range(10, 100):

        digit_sum = 0
        for d in str(num):
            digit_sum += int(d)

        if digit_sum + digit_sum ** 2 == num:
            print(num)

def main():
    print_result()

if __name__ == "__main__":
    main()
