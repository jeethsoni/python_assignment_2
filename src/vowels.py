"""
A python script to uppercase vowels in user entered string

@usage python3 vowels.py "Hey, I am jeet, I love programming
"""


def main():

    # vowels list
    vowels = ["a", "e", "i", "o", "u"]

    string = input("enter a long string: ").lower()  # user input

    # check for each letter in string and uppercase vowels
    for s in string:
        if (s in vowels):
            new_char = s.upper()  
            print(new_char, end="")
        else:
            print(s, end="")

    print("\n")


if __name__ == "__main__":
    main()
