import book as bk
import time
import string as st

class NoRoomError:
    pass

class shelf_dictionary():
    def __init__(self):
        self.shelf_id = {}
        for letter in st.ascii_lowercase:
            self.shelf_id[letter] = 0
    def newId(self,letter):
        self.shelf_id[letter] +=1
        return self.shelf_id[letter]



class shelf():
    _shelf_ids = shelf_dictionary()

    def __init__(self,letter ,books=[], size=150 ):
        self.__letter  = letter.lower()
        self.__size=size
        self.books = []
        self.__bookNames = []
        self.__writersNames = []
        self.__remaining_size = size
        self.__shelfId = shelf.newshelfId(letter)
        self.__shelf_writers_katalog ={}

        self.__counter = 0
        try:
            for member in books:
                self.addBook(member)

        except IndexError as e:
            print(e)
            raise
        except Exception:
            raise

    def __iter__(self):
        self.__counter = 0
        return self

    def __next__(self):
        if self.__counter <= len(self.books):
            current = self.__counter
            self.__counter += 1
            return self.books[current].bookName
        else:
            raise StopIteration

    def check_validity(self,newBook):
        firstLetter = newBook.writerName[0].lower()
        if firstLetter != self.__letter:
            raise ValueError ("the writer '{}' does not belong to this shelf".format (newBook.writerName))
        elif newBook.writerName not in self.__shelf_writers_katalog.keys():
            self.__shelf_writers_katalog[newBook.writerName] =[newBook.bookName]
            self.__writersNames.append(newBook.writerName)
        elif newBook.bookName in self.__bookNames :
            raise ValueError ("the book '{}' allready exists on this shelf".format (newBook.bookName))
        else:
            self.__shelf_writers_katalog[newBook.writerName].append(newBook.bookName)

    def addBook(self,member):
        remaining_size  = self.get_remaining_size(member, 'add')
        try:
            if  remaining_size <= 0:
                raise NoRoomError("There is no more room in this shelf")
            else:
                self.check_validity(member)
                self.books.append(member)
                bookName = member.bookName
                self.__bookNames.append(bookName)
                self.__remaining_size = remaining_size
        except ValueError as e:
            print(e)
            raise
        except NoRoomError as e:
            print ("There is no more room for this book")
            raise
        finally:
            self.sortBooks()

    def removeBook(self, bookName):
        try:
            bookIndex    = self.return_book_index(bookName)
            bookToRemove = self.books[bookIndex]
            writerName   = bookToRemove.writerName
            self.__remaining_size = self.get_remaining_size(bookToRemove,'remove')
            self.__shelf_writers_katalog[writerName].remove(bookName)
            self.books.pop (bookIndex)
            self.__bookNames.pop(bookIndex)
        except Exception as e:
            print (e)
            raise
        finally:
             self.sortBooks()

    def return_book_index(self,bookName):
        if bookName in self.__bookNames:
            return self.__bookNames.index(bookName)
        else:
            return None

    def return_book(self,bookIndex):
        if self.books[bookIndex]:
            return self.books[bookIndex]
        else:
            return None

    def get_remaining_size(self, newBook, action='add'):
        book_size = ((3/500) * newBook.number_of_pages +0.5)
        if action == 'add':
            remaining_size = self.__remaining_size - book_size
        else:
            remaining_size = self.__remaining_size + book_size
        return remaining_size


    def __gt__(self, other):
        return self.self.__shelfId > other.return_shelf_id

    def sortBooks(self):
        if len(self.books) <=1:
            return
        self.__writersNames.sort()
        self.books.sort(key= lambda x: x.return_book_key)

        self.__bookNames.clear()
        for writer in self.__writersNames:
            bookslist = self.__shelf_writers_katalog[writer]
            bookslist.sort()
            for currentBook in bookslist:
                self.__bookNames.append(currentBook)
    def return_writers_names(self):
        return  self.__writersNames
    def booksForWriter(self,writerName):
        if writerName not in self.__shelf_writers_katalog.keys():
            return 0
        else:
            return len(self.__shelf_writers_katalog[writerName])

    def printshelf(self):
        for book in self.books:
            print(book)
            #print (str(book) +"  Shelf:"+ self.__letter +":" + str(self.__shelfId)+"\n")

    @property
    def return_shelf_id(self):
        return self.__shelfId
    @property
    def return_shelf_letter(self):
        return self.__letter
    @property
    def return_shelf_size(self):
        return self.__size

    @property
    def book_names_for_shelf(self):
        tempBooksArr = []
        for member in self.books:
            tempBooksArr.append(member.bookName)
        return tempBooksArr

    @classmethod
    def newshelfId(cls,letter):
        letter = letter.lower()
        newId = cls._shelf_ids.newId(letter)
        return newId


