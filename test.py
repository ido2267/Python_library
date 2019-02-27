from book import *
from shelf import *
import liberary as lib
from validateuser import *
import logfile as lg
import reader as rd

book100 = Book("Harry Potter and the Philosopher's Stone","J. K. Rowling", 980)
book101 = Book("Harry Potter and the Chamber of Secrets","J. K. Rowling", 820)
book102 = Book("Harry Potter and the Prisoner of Azkaban","J. K. Rowling", 810)
book103 = Book("Harry Potter and the Half-Blood Prince","J. K. Rowling", 800)
book104 = Book("Harry Potter and the Order of the Phoenix","J. K. Rowling", 780)
book105 = Book("Harry Potter and the Goblet of Fire","J. K. Rowling", 780)
book106 = Book("Harry Potter and the Deathly Hallows","J. K. Rowling", 740)
book107 = Book("The animal farm" ,"George Orwell", 680)
book108 = Book("1984","George Orwell", 610)
book109 = Book("Pride and Prejudice","Jane Austen", 600)
book110 = Book("To Kill a Mockingbird","Harper Lee", 580)
book111 = Book("The Da Vinci Code","Dan Brown", 580)
book112 = Book("The Catcher in the Rye","J. D. Salinger", 560)
book113 = Book("The Great Gatsby","F. Scott Fitzgerald", 530)
book114 = Book("Twilight","Stephenie Meyer", 470)
book115 = Book("The Hunger Games","Suzanne Collins", 450)
book116 = Book("Jane Eyre","Charlotte Brontë", 440)
book117 = Book("The Kite Runner","Khaled Hosseini", 430)
book118 = Book("Animal Farm","George Orwell", 430)
book119 = Book("Brave New World","Aldous Huxley", 400)
book120 = Book("The Lord of the Rings","J. R. R. Tolkien", 390)
book121 = Book("The Fellowship of the Ring","J. R. R. Tolkien", 380)
book122 = Book("Fahrenheit 451","Ray Bradbury", 380)
book123 = Book("Angels & Demons","Dan Brown", 370)
book124 = Book("New Moon","Stephenie Meyer", 370)
book125 = Book("Wuthering Heights","Emily Brontë", 370)
book126 = Book("The Curious Incident of the Dog in the Night-Time","Mark Haddon", 370)


arr = [book100,book102,book103,book104,book105,book106,book107,book108,book109,book110,book111,
 book112,book113,book114,book115,book116,book117,book118,book119,book120,book121,book122,book123
 ,book124,book125,book126]
avi = rd.Reader("avi", 2)
rina = rd.Reader("Rina", 3)
readersArr = [avi,rina]
myLib = lib.Liberary(arr)
myLib.place_book_on_shelf(book101)

myLib.addReader(readersArr)
myLib.give_reader_a_book("avi",'To Kill a Mockingbird')
myLib.give_reader_a_book("avi",'The Catcher in the Rye')
myLib.give_reader_a_book("Rina",'Harry Potter and the Chamber of Secrets')

myLib.recieve_book_from_reader("avi",'The Catcher in the Rye')
myLib.printLiberary()
