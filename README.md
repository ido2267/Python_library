# Python_library
My interpetation for the exerciseI did in the end of the python course by Yaniv Arad
To check this at work you should download the files. execute file main.py and type 
the user name 'ido' and the password: 123

Here are the demands of the exercise:

A.
Write the following classes (in different modules):

Class Book:
Properties:
Book's name
Writer's name
Number of pages
Borrowed = True/False

Functions:
Constructor (receives book's name, writer's name , number of pages)
Print information (prints book's name, writer's name, number of pages) 



Class Shelf:
Properties:
Letter – only writer's that their name starts with that letter will be presented on this shelf
Shelf's size – the number of books it can contain (isn't it more logical to count the pages?)
Books (an array of elements of class 'Book')
Shelf number. There can be more than one shelf for every letter

Functions:
•	Constructor (receives shelf letter, An array of books [ in default the array will be empty] , size of shelf )
•	Get books for writer (gets a writer name and returns the books for that writer)
•	Add a book (receives a book, if the writer's name starts with the right letter and there is a room for that book  it will add the book to the array and marked Borrowed as False)
•	Replace a book (receives  a new book and an old book's name. replace the old book that is on the shelf with the new book)
•	Sort (will sort the book's array by writers' names and the books for every writer inside the name
 

Class Reader:
Properties:
Name   
Number of books allowed
Loans – a dictionary where the book name is the key and the date of loaning the book is the value
Approved – a value that is True if the user is allowed to take a new book and False if he has the maximum books allowed or that he have a book for too long

Functions:
•	Constructor (receives reader's name  ,An array of books names ,[ in default the array will be empty] , Number of books allowed )
•	Take a book  (gets a book name and keep the book's name in Loans with the date)
•	Give a book  (gets a book name and delete the book's name in Loans)


Class Library:
Properties:
Number of shelves (that can be changed)
Shelves – an array of items from class 'Shelf'
Storage – an array of books that are not on any shelf

Functions:
•	Constructor (receives  an array of shelves,[ in default the array will be empty] , number of shelf )
•	Print books for writer (gets a writer name and prints the books for that writer in every shelf)
•	Print library (prints all library in parallel threads)
•	Replace a book (receives  a new book and an old book's name. replace the old book that is on the shelf with the new book)
•	Sort (will sort the book's array by writers names and the books for every writer inside the name
Program:
Write a program that presents to the user (with infinite loop):
1.	 Add a book (ask the user for book's details)
2. add a reader
3. give reader a book
4. recieve a book from reader
5.	Replace a book (receives the name of the returned book and the name of the 
Book that is given
6.	Print books for a writer (receives the writer's name)
7.	Print the entire liberaray
8.	Exit the program

Write to a log file the starting time and ending time of the program
Create a log in system to the program – the user will have to insert name and password that are kept in a file

