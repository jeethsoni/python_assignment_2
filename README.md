# Python Assignment 2
*Author: Jeet Soni*

*Date: 07/28/2023*

---
### **1) Ask user to enter some text and write it to a text file use python to read the file and print the output line by line. Use python to append more text to the same file. Ask user for more text until user says I'm tired I am done.**

My first file handling python script where I make the file generate by itself and ask user to enter some text whatever they want and write that to a file and print to the console as well. It's like magic how the file appears in the directory after I run the python file. 

I used input function to get the text and open() function to open the file and used "w+" access mode to write and read the file. Then if user wanted to add more text to the file. I used a while loop to keep asking the user if they want to add more text if yes then keep the while loop running otherwise exit the program. 

### **2) Take the sample file created above, read the content, insert that content into new file with some added content to it.**

So now, I want a copy of the file I created and want to keep a backup of the file. What can I say?, I lose stuff easily. Well I wrote a program that will take that file with all the contents in it and make copy it to a new file.
This time, user will be given option one to add(append) to the file once. Now I have a backup. WooHoo.

The way I implemented is, I used nested with open(). First, read the file that already exists and make a copy file to write to it. I used a for loop to read the existing file's content line by line and write that to the new backup file. Then I gave user the option if they want to write more to the backup file. If yes, then I used "a" (append) access mode to append to the file from new line.

### **3) Enter 10 numbers, loop through, if even multiple that by 100 (use continue in the for loop) print that new number that was multiplied by 100.**

When I learned about continue loop. It was confusing but when I solved this question, it was really easy to understand. This program will take 10 digits from the user comma separated. Then it will multiply the even by 100 and continue if it's odd (don't do anything)

The way I solved this is, I asked user to enter 10 numbers in one line and used .split() to separate each number with a comma (,). I checked if the user entered exactly 10 numbers using len() function. I also used regular expression to fix the spacing of the numbers that user entered to keep the program from throwing errors. I also validated user input, If user entered anything other than numbers then, exit the program. 

If it passes all the rules, I converted those numbers to integer using map() function to iterate over each number and then used list() to store those numbers in a list. Then I used for loop to iterate through each numbers in list, if it's odd then **continue** else multiply the number (even) by 100. Finally, print those new numbers. 

### **4) Enter 10 numbers, from 50 to 200 sort the list from the 10 numbers inputted then when looping print each number but break the loop if number is more than 100.**

A program to that will let user enter 10 numbers between 50 and 200. The script will check if the numbers between 50 to 200. If not, then it will exit out. I checked that with for loop by looping through every number in the list and checking if they in range. If everything checks out at last, I looped through each number in the list to break the loop if more than 100 and print the numbers before the loop was broken.

### **5) Ask user to enter a long string, find the index of vowels, whatever vowels found convert that to uppercase and print the final string.**

A program that will uppercase all the vowels in user entered string. I solved this problem 3 different ways:

* **Single for loop and if-else statement**

First, I created a list with vowels. Then I asked user to enter string using input() function and lowered the string using lower() function. I used a simple for loop to loop through each letter in string and checked if that letter matches any letter in vowels. If yes, then make it uppercase using upper() function and print it else print the current letter. 

* **Index in the list**

I asked user to enter the string and then converted that string into a list() using list built-in function. I used a for loop to find the length of list. Inside that for loop I used if statement to match the letter in the vowels. If yes, then change that current letter at that index and make that letter uppercase. Finally, I printed the final string using for loop.

* **List comprehension**

This is the shortest solution of all. I simply used list comprehensions to solve this. I converted user input into list. To perform list comprehensions, I made a new variable new_string and used for loops and if-else statements. After that new string list is created with uppercase vowels I simply used for loop to iterate over every item in the new_string list and print the final string.

### **6) Write a python script to create a dictionary of recipe or whatever and write that dictionary to a file as a json document (prettify the json file).**  

A program that will copy your favorite recipe dishes to a pretty json document. I used dictionaries and list inside a dictionary to make this beautiful recipe json document. I simple created two cuisines: mexican and indian and stored those dictionaries into recipe variable.

I used with open() with "w" access mode to open the file and within it I used json.dump() to dump that recipe dictionary into the json file and indented it by 4. 

---

This is my explanation for all the problem.

Open for suggestions

Jeet Soni

Cheers










