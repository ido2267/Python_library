import book as bk
import reader as rd
from datetime import datetime

def load_books(fileName):
    bookArray = []
    try:
        with open(fileName, "r") as book_database:
          buffer = book_database.read()
          arr = buffer.split('\n')
          for line in arr:
              if line:
                  bookName, writer,   pages = line.split(';')
                  newBook = bk.Book (bookName,writer,int(pages))
                  bookArray.append(newBook)

    except FileNotFoundError as e:
        print (e)
    except Exception:
        raise
    finally:
        return bookArray

def store_books(fileName,bookArray):
    try:
        with open(fileName, "w") as book_database:
           for book in bookArray:
              writerName = book.writerName
              bookName = book.bookName
              pages = book.number_of_pages
              line =   bookName + ';' + writerName +';' + str(pages)
              book_database.write(line+ '\n')
    except ValueError as e:
        print (e)
        raise
# /////////////////////////////////
def load_readrs(fileName):
    readerArray = []
    try:
        with open(fileName, "r") as readers_database:
          buffer = readers_database.read()
          readers = buffer.split('\n')
          for line in readers:
              if line:
                  arr = line.split(';')
                  readerName = arr[0]
                  booksAllwoed = int(arr[1])
                  newReader = rd.Reader(readerName,booksAllwoed)
                  index = 2
                  while index < (len(arr) -1):
                      bookName = arr[index]
                      dateBorrowed = datetime.strptime(arr[index+1], '%Y/%m/%d')
                      newReader.addBook(bookName,dateBorrowed)
                      index +=2
                  readerArray.append(newReader)
          return readerArray
    except FileNotFoundError as e:
        print (e)
    except Exception:
        raise

# //////////////////////////////////
def store_readers(fileName, readersArray):
    try:
        with open(fileName, "w") as readers_database:
           for reader in readersArray:
              readerName  = reader.reader_name
              booksAllwoed = reader.books_allowed
              line =  readerName +';' + str(booksAllwoed)
              readerDict = reader.borrow_list
              for bookName in readerDict.keys():
                  date_taken = readerDict[bookName]
                  line += ';' + bookName +';' + date_taken
              readers_database.write(line +'\n')
    except ValueError as e:
        print (e)
        raise
