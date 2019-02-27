import shelf as sh
import book as bk
from ThreadMenage import *
from reader import *
import string as st


class Liberary():
    def __init__(self, booksArray = [], limit_of_shelves=1000):
        self.__limit_of_shelves = limit_of_shelves
        self.__shelvesDict = {}
        self.__shelvesIdDict = {}
        self.__counter = 0
        self.__storage = []
        self.__storage_bookNames = []
        self.__readers=[]
        self.__reader_names=[]
        for letter in st.ascii_lowercase:
            self.__shelvesDict[letter] = []
            self.__shelvesIdDict[letter] = []
        for newBook in booksArray:
            self.place_book_on_shelf(newBook)

    def __iter__(self):
        self.__counter = 0
        return self

    def __next__(self):
        if self.__counter < len(self.__shelvesIdDict):
            current = self.__counter
            self.__counter += 1
            return self.__shelvesIdDict[current]
        else:
            raise StopIteration

    def remove_shelf(self,letter, shelfId):
        i = self.__shelvesIdDict[letter].index(shelfId)
        self.__storage +=  self.__shelvesDict[letter][i].books
        self.__shelvesIdDict[letter].pop(i)
        self.__shelvesDict[letter].pop(i)

    def addshelf(self, newshelf):
        total_shelves = len(self.__shelvesDict.values())
        if total_shelves >= self.__limit_of_shelves:
            raise IndexError("There are no more shelves available. Add more shelves first")
        letter = newshelf.return_shelf_letter
        shelfId= newshelf.return_shelf_id
        self.__shelvesDict[letter].append(newshelf)
        self.__shelvesIdDict[letter].append(shelfId)

    def addReader(self,readersArray):
        for reader in readersArray:
            self.__readers.append(reader)
            self.__reader_names.append(reader.reader_name)

    def increase_shelves_limit(self, shelves_to_add):
        self.__limit_of_shelves += shelves_to_add
        
    def decrease_shelves_limit(self,shelves_to_remove):
        if shelves_to_remove > self.__limit_of_shelves:
            raise IndexError ("You can not diminsh {} shelves from a liberary that has only {} shelves"
                              .format(shelves_to_remove, self.__limit_of_shelves))
        empty_shelves = self.__limit_of_shelves - len(self.__shelvesDict.values())
        gap = shelves_to_remove  - empty_shelves
        if gap > 0 :
            raise IndexError("You can not decrease {} shelves before removing {} shelves first from liberary "
                             .format(shelves_to_remove, gap))
        else:
            self.__limit_of_shelves -= shelves_to_remove

    def booksForWriter(self,writterName):
        total = 0
        letter = writterName[0].lower()
        for member in self.__shelvesDict[letter]:
            total+= member.booksForWriter(writterName)
        print ("The total numbers of books for writter {} is {}".format (writterName, str(total)))

    def locate_book_on_shelf(self,bookName):
        for shelvesList in self.__shelvesDict.values():
            for shelf in shelvesList:
                bookIndex = shelf.return_book_index(bookName)
                if bookIndex==None:
                    pass
                else:
                    letter = shelf.return_shelf_letter
                    shelfIdIndex = self.__shelvesIdDict[letter].index(shelf.return_shelf_id)
                    return (letter,shelfIdIndex,bookIndex)
        return None

    def give_reader_a_book(self,readerName, bookName):
        if readerName in self.__reader_names:
            try:
                letter, shelfIdIndex, bookIndex  = self.locate_book_on_shelf(bookName)
                readerIndex = self.__reader_names.index(readerName)
                self.__readers[readerIndex].addBook(bookName)
                bookRequested = self.__shelvesDict [letter][shelfIdIndex].return_book(bookIndex)
                self.__storage.append(bookRequested)
                self.__storage_bookNames.append(bookName)
                self.__shelvesDict[letter][shelfIdIndex].removeBook(bookName)
            except Exception as e:
                raise ValueError("no such book on any shelf")
        else:
            raise ValueError("No such reader in the list")

    def recieve_book_from_reader(self,readerName, bookName):
        try:
            bookIndex = self.__storage_bookNames.index(bookName)
            bookToReturn = self.__storage[bookIndex]
            self.place_book_on_shelf(bookToReturn)
            self.__storage.pop(bookIndex)
            self.__storage_bookNames.remove(bookName)
            readerIndex = self.__reader_names.index(readerName)
            self.__readers[readerIndex].removeBook(bookName)
        except Exception as errorMessage:
            print (errorMessage)
            raise

    def printLiberary (self):
        threadsArray = []
        for letter in self.__shelvesDict:
            for member in self.__shelvesDict[letter]:
                threadsArray.append(libThread(member.printshelf))
        for member in threadsArray:
            member.start()
        for member in threadsArray:
            member.join()

    def place_book_on_shelf(self,book):
        writerName = book.writerName
        firstLetter = writerName[0].lower()
        try:
            self.__shelvesDict[firstLetter][-1].addBook(book)
        except :
            newShelf = sh.shelf(firstLetter,[book])
            self.addshelf(newShelf)
        finally:
            self.sort_book_on_shelves(firstLetter, -1)

    def sort_book_on_shelves (self,letter,index):
        firstId= self.__shelvesDict[letter][0].return_shelf_id
        currentId = self.__shelvesDict[letter][index].return_shelf_id
        while currentId > firstId:
            prevIndex = index -1
            prevBook = self.__shelvesDict[letter][prevIndex].books[-1]
            currBook = self.__shelvesDict[letter][index].books[0]
            if prevBook > currBook:
                self.__shelvesDict[letter][prevIndex].removeBook(prevBook.bookName)
                self.__shelvesDict[letter][prevIndex].addBook(currBook)
                self.__shelvesDict[letter][index].removeBook(currBook.bookName)
                self.__shelvesDict[letter][index].addBook(prevBook)
                self.__shelvesDict[letter][index].sortBooks
                self.__shelvesDict[letter][prevIndex].sortBooks
              # keep executing recursively
            else:
                return

            self.sort_book_on_shelves(letter,prevIndex)

        self.__shelvesDict[letter][index].sortBooks


    def return_shelf(self,Id, letter):
        if id in self.__shelvesIdDict[letter]:
            place = int(Id)
            return self.__shelvesDict[letter][place]
        else:
            return None


    @property
    def readersNames(self):
        return self.__reader_names

    def books_for_reader(self,readerName):
        if readerName not in self.__reader_names:
            return None
        index = self.__reader_names.index(readerName)
        reader = self.__readers[index]
        return reader.book_list

    def return_shelf_books(self):
        booksArray = []
        for letter in self.__shelvesDict.keys():
            for shelf in self.__shelvesDict[letter]:
                for book in shelf.books:
                    booksArray.append(book)
        return booksArray

    def return_storage_books(self):
        return self.__storage

    def return_all_readers(self):
        return  self.__readers

    def load_storage(self,booksArray):
        for book in booksArray:
            self.__storage.append(book)
            self.__storage_bookNames.append(book.bookName)