"""
A python script to uppercase vowels in string using list indexing

@usage python3 list_index.py "I am an awesome programmer"
"""


def main():

    # user string input stored as list
    strings = list(input("Enter a string: ").lower())
    vowels = ["a", "e", "i", "o", "u"]

    # for loop to iterate through the characters in string
    for s in range(len(strings)):
        if (strings[s] in vowels):
            upper_char = strings[s].upper()  # if matches uppercase the vowel
            strings[s] = upper_char  # at that index change it to uppercase

    # iterate over the list and print it
    print("your final string with vowels uppercased is: ")
    for string in strings:
        print(string, end="")

    print("\n")


if __name__ == "__main__":
    main()
