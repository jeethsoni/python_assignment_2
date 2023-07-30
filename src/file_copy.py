"""
a python script that will add user entered text to a file

@usage python3 file_copy.py "Programming is fun. I love it."
"""


def main():

    # open the file to read it, write it to another file
    with open("user_file.txt", "r") as rf:
        with open("user_file_copy.txt", "w") as wf:
            for line in rf: 
                wf.write(line)
    print("file copied")

    # ask user to if they want to add more content to the file
    copy_file = open("user_file_copy.txt", "a")
    choice = input("Do you wish to add more text? yes/no: ").lower()
    if choice == "yes":
        text = input("Add more text here: ")
        copy_file.write("\n" + text)
        copy_file.close()

    else:
        print("bye")


if __name__ == "__main__":
    main()
