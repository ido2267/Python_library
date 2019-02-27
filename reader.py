from datetime import datetime

class noMoreBooks():
    pass
class borrowOverdue():
    pass
class Reader():

    def __init__(self, name, number_of_books_allowed=2):
        self.__name = name
        self.__numAllowed= number_of_books_allowed
        self.__borrows={}
        self.__books_taken = 0
        self.__days_to_return = 21

    def addBook(self,bookName, date_Taken = datetime.now()):
        try:
            self.approveReader()
            date_taken_str = date_Taken.strftime("%Y/%m/%d")
            self.__borrows[bookName] = date_taken_str
            self.__books_taken += 1
            return True
        except Exception as e:
            print (e)
            raise

    def removeBook(self, bookName):
        del(self.__borrows[bookName] )
        self.__books_taken -= 1


    def approveReader(self):
        if self.__books_taken >= self.__numAllowed:
            raise noMoreBooks("No more books allowed for {}".format(self.__name))
        for borrowDate in self.__borrows.values()  :
            date_borrowed =   datetime.strptime(borrowDate, "%Y/%m/%d")
            delta = datetime.now() - date_borrowed
            if delta.days > self.__days_to_return:
                raise borrowOverdue("The time for returning a book  has passed")

    def change_number_of_books_allowed(self, amount):
        self.__numAllowed = amount

    def change_period_allowed(self, newPeriod):
        self.__days_to_return = newPeriod
    @property
    def reader_name(self):
        return self.__name
    @property
    def book_list(self):
        return self.__borrows.keys()
    @property
    def borrow_list(self):
        return self.__borrows
    @property
    def books_allowed(self):
        return self.__numAllowed

