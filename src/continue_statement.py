"""
A python script that will multiply the even number by 100

@usage python3 continue_statement.py 1,2,3,4,5,6,7,8,9,10
"""
import re
import sys


def main():

    # enter 10 numbers comma seperated
    numbers = input("Enter 10 numbers (with comma ,): ").split(",")

    # if user entered 10 numbers proceed
    if (len(numbers) == 10):
        for n in numbers:
            new_number = re.sub(r"\s+", "", n)  # removes white space globally
            # checks if user entered digits or not
            if (new_number.isnumeric() is False):
                sys.exit("Sorry, you didn't enter an integer, please run it again")  # noqa
        number = list(map(int, numbers))  # converts string numbers to integer

        # if odd then print odd and if even then multiply the numbers by 100
        for n in number:
            if (n % 2 != 0):
                print(n)
                continue

            new_even = n * 100
            print(f"new Even: {new_even}")


if __name__ == "__main__":
    main()
