"""
A python script that uses break statement to break the loop if number is more
than 100

@usage python3 break_statement.py 51, 52, 61, 100, 114, 116, 156, 69, 192, 194
"""
import sys


def main():

    # user enters 10 numbers with comma seperated
    numbers = input("Enter 10 numbers from 50 to 200: "). split(",")

    # if user entered 10 numbers proceed else exit
    if (len(numbers) == 10):
        conver_number = list(map(int, numbers))  # convert to integer
        for n in conver_number:
            if (n < 50 or n > 200):
                print(f"invalid input: {n}")
                sys.exit("sorry, you didn't enter between 50 to 200")

        for n in conver_number:
            if (n >= 100):
                break
            else:
                print(n)
    else:
        print("sorry you didn't enter 10 numbers")


if __name__ == "__main__":
    main()
