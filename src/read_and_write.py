"""
A python script to to write to a file till user says i'm done

@usage python3 read_and_write.py "Hi, I am awesome"
"""
import sys


def main():

    # ask user to write some text and add that to a file
    continue_writing = True
    string = input("Write some text: ")
    user_file = open("user_file.txt", "w+")
    user_file.write(string)
    user_file.flush()
    user_file.seek(0)  # change the pointer in file
    print("File contents:", "\n" + user_file.read())  # print the content to the file  # noqa
    user_file.close()

    # ask user if they want to continue writing to file
    while continue_writing:
        choice = input("Do you want to continue writing? (yes/no): ").lower()
        if (choice == "yes"):
            new_string = input("Add more text here: ")
            user_file = open("user_file.txt", "a+")
            user_file.write("\n" + new_string)
            user_file.flush()
            user_file.seek(0)
            print("File contents:", "\n" + user_file.read())

        else:
            user_file.close()
            sys.exit("Thank you for using our program, Bye Bye")


if __name__ == "__main__":
    main()
