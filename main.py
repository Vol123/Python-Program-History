from MySQL import StdCommandPrint
from MySQL import Adress
from MySQL import Book
from MySQL import Person
from MySQL import SQLVirtual

varPrintTables = StdCommandPrint()

adresses = [
        Adress("Warszawa", "Szczwnicka", 12, 3),
        Adress("Warszawa", "Towarowa", 35, 7),
        Adress("Krakow", "Piekna", 42, 13),
        Adress("Warszawa", "Smaczna", 13, 2)
    ]
varPrintTables.printAdresses(adresses)

books = [
        Book("Glowa na tranzystorach", "Jasiek Mela", 205),
        Book("Matematyka", "Wojciech Babanski i tp.", 312),
        Book("C++", "Haland Fustecki", 1220)
    ]
varPrintTables.printBooks(books)

persons = [
        Person("Haleta Andżej", "Programist", 1230.23, [1], [0, 1, 2]),
        Person("Staciuk Ivan", "Uczen", 0.0, [0], [0, 1]),
        Person("Borow Pietia", "Biolog", 500.345, [2], [0]),
        Person("Jacki Wasia", "Matematyk", 809.234, [3], [1, 2])
    ]
varPrintTables.printPersons(persons)

resultTable = SQLVirtual(adresses, books, persons).LEFTJOIN()
varPrintTables.printResultTable(resultTable)
input()