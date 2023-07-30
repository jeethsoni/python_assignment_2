"""
A python script to uppercase vowels using list comprehension

@usage python3 list_comprehension.py "programming is frustrating but thrilling and fun"  # noqa
"""


def main():

    # user input into a list
    strings = list(input("Enter a string: ").lower())
    vowels = ["a", "e", "i", "o", "u"]

    # list comprehension to uppercase the vowels in list
    new_string = [s.upper() if s in vowels else s for s in strings]

    # print the final list
    print("Your final string is: ")
    for ns in new_string:
        print(ns, end="")

    print("\n")


if __name__ == "__main__":
    main()
