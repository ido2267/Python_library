from book import *
from shelf import *
import liberary as lib
from validateuser import *
import logfile as lg
from reader import *
import handle_storage as ld

shelvedBooks = "bookdatabase.txt"
readerStorage = "readerDatabase.txt"
unShelvedBooks = "bookStorage.txt"

shelvesArr = ld.load_books(shelvedBooks)
unShelvesArr = ld.load_books(unShelvedBooks)

readersArr = ld.load_readrs(readerStorage)
if shelvesArr:
    myLib = lib.Liberary(shelvesArr)
else:
    raise ValueError("no books in liberary")
if readersArr:
    myLib.addReader(readersArr)
if unShelvesArr:
    myLib.load_storage(unShelvesArr)

def newBook():
    stage = [True, True, True]
    while True:
        if stage[0]:
            bookName = input("Enter the book's name: ")
            stage[0] = False
        elif stage[1]:
            author = input("Enter The author name:  ")
            stage[1] = False
        elif stage[2]:
            number_of_pages = input("Enter The number of pages:  ")
            if number_of_pages.isnumeric():
                number_of_pages = int(number_of_pages)
                stage[2] = False
            else:
                print("Numeric input needed")
        else:
            newbook = Book(bookName, author, number_of_pages)
            return newbook

def newReader():
    stage = [True, True]
    while True:
        if stage[0]:
            readerName = input("Enter the reader's name: ")
            stage[0] = False

        elif stage[1]:
            number_of_books_allwoed = input("Enter The number of books allwoed for {}:  ".format(readerName))
            if number_of_books_allwoed.isnumeric():
                number_of_books_allwoed = int(number_of_books_allwoed)
                stage[1] = False
            else:
                print("Numeric input needed")
        else:
            newreader = Reader(readerName, number_of_books_allwoed)
            return newreader
def getReaderName():
    counter = 0
    while counter < 4:
        reader_name = input("Enter the reader's Name: ")
        if reader_name not in myLib.readersNames:
            print("No such reader in the liberary.")
            counter +=1
        else:
            return reader_name
    print("Too many attampts, You are being returned to main menu")
    return None

def book_from_reader(readerName):
    counter = 0
    while counter < 4:
        bookFromReader = input("Type in the book you are returning: ")
        bookList = myLib.books_for_reader(readerName)
        if bookFromReader not in bookList:
            print("No such book for that reader.")
            counter += 1
        else:
           return bookFromReader
    print("Too many attampts, You are being returned to main menu")
    return None
def book_to_reader():
    counter = 0
    while counter < 4:
        bookToReader = input("Type in he book you are taking: ")
        if not  myLib.locate_book_on_shelf(bookToReader):
            print("No such book in the liberary.")
            counter += 1
        else:
            return bookToReader
    print("Too many attampts, You are being returned to main menu")
    return None

def changeBook():
    reader_name = getReaderName()
    if reader_name:
        bookFromReader = book_from_reader(reader_name)
        if bookFromReader:
            bookToReader = book_to_reader()
            if bookToReader:
                return reader_name, bookFromReader, bookToReader
    return None

 
def execMenu(num):

    def add_book():
        new_book  =newBook()
        myLib.place_book_on_shelf(new_book)
    def add_reader():
        new_reader = newReader()
        myLib.addReader([new_reader])
    def change_book():
        reader_name, bookFromReader, bookToReader = changeBook()
        if reader_name:
            try:
                myLib.recieve_book_from_reader(reader_name,bookFromReader)
                myLib.give_reader_a_book(reader_name,bookToReader)
            except Exception as e:
                print(e)
    def give_book_to_reader():
        reader_name = getReaderName()
        bookToReader = book_to_reader()
        myLib.give_reader_a_book(reader_name, bookToReader)

    def receive_book_from_reader():
        reader_name = getReaderName()
        bookFromReader = book_from_reader(reader_name)
        myLib.recieve_book_from_reader(reader_name, bookFromReader)

    def print_books_for_writter():
        writter = input ("Type writter's name: ")
        myLib.booksForWriter(writter)

    def print_liberary():
        myLib.printLiberary()

    def numbers_to_actions(argument):
        switcher = {
            1: add_book,
            2: add_reader,
            3: give_book_to_reader,
            4: receive_book_from_reader,
            5: change_book,
            6: print_books_for_writter,
            7: print_liberary }
        return switcher.get(argument, "Invalid option")
    func = numbers_to_actions(num)
    func()


counter=0
firstLoop = True
mainLoop = False

lg.reportToLog('Starting time')
while firstLoop:
    username = input("Enter user name:  ")
    password = input ("Enter your password:  ")
    if validateUser(username, password):
        print("Welcome")
        mainLoop = True
        firstLoop = False
    else:
        if counter >= 3:
            firstLoop = False
            print("Too many attampts. You are being disconnected. ")
        else:
            print ("Wrong user name or password. try again")
            counter +=1
counter=0

while mainLoop:
    action = input (' Choose desired action:\n 1.Add a book.\n '
           '2.Add a reader.\n 3.Give a book to reader \n 4.Receive book from reader.\n'
            ' 5.Replace a book\n 6.Print number of books for a writter\n 7.Print the entire liberary\n 8.Exit\n' )

    if action.isnumeric():
        action = int(action)
        if action in range(1,8):
            execMenu(action)
        elif   action  == 8:
            ld.store_books(shelvedBooks, myLib.return_shelf_books())
            ld.store_books(unShelvedBooks,myLib.return_storage_books())
            ld.store_readers(readerStorage, myLib.return_all_readers())
            mainLoop = False
        else:
            if counter >= 3:
                mainLoop = False
                print("Too many attampts. You are being disconnected. ")
            else:
                print ("Wrong choice. try again")
                counter +=1
    else:
        print ("You have to choose a number between 1 and 6")



lg.reportToLog('Ending time')



#myLib.remove_shelves([sh2, sh3])

#myLib.decrease_shelves_limit (2)
#3412
# myLib.booksForWriter("George Orwell")
#sh2.printshelf()
# myLib.printLiberary()
# for member in myLib:
#     print(member)

# while True :
#     num = int(input("Enter number"))
#     if num not in arr:
#         arr.append(num)
print ("End of program")


