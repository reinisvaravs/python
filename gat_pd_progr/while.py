
def main():
    start = 2000
    interest = 4
    end = 3000
    year = 0
    while start < end:
        start *= (interest / 100 + 1)
        year += 1
    print(f"years taken: {year}. End sum: {end}.")

if __name__ == "__main__":
    main()
