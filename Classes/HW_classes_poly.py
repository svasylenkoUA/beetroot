class Animal:

    def __init__(self, name):
        self.name = name

    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print("Wof woof")

class Cat(Animal):
    def talk(self):
        print("meow")

def talk_function(who):
    return who.talk()

d1 = Dog("Peter")
c1 = Cat("Alice")
d1.talk()
c1.talk()
print("--------")
talk_function(d1)
talk_function(c1)

# ************************************************

class Library:
    def __init__(self, name, books=[], authors = []):
        self.name = name
        self.authors = authors
        self.books = books

    def new_book(self, name: str, year: int, author):
        self.name = name
        self.year = year
        self.author = author
        self.books.append(name)

    def group_by_author(self, author):
        return self.books.sort(key = author.name)

    def group_by_year(self, year: int):
        return self.books.sort(key = year)

class Author:

    def __init__(self, name, country, birthday, books=[]):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __repr__(self):
        return self.name + " " + self.birtday + " " + self.country + ":" + self.books

    def __str__(self):
        self.__repr__()

class Book(Author):
    total_books = 0
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.total_books +=1

    def __repr__(self):
        return self.name + " " + self.author.name + " " + self.year

    def __str__(self):
        self.__repr__()


author1 = Author("J. Smith", "UK", "Dec 2021", "")
book1 = Book("Harry Potter", 2020, a1)
Library.new_book("Harry Potter", 2020, a1)
print("11")

# class Fraction:
#     def __init__(self, arg):
#         try:
#             self.value = float(arg)
#         except ValueError:
#             print("Value error")
#
#     def __add__(self, other):
#         try:
#             return self.value + float(other.value)
#         except ValueError:
#             print("Value error")
#
#     def __le__(self, other):
#         try:
#             return self.value - float(other.value)
#         except ValueError:
#             print("Value error")
#
#     def __mul__(self, other):
#         try:
#             return self.value * float(other.value)
#         except ValueError:
#             print("Value error")
#
#     def __divmod__(self, other):
#         try:
#             return self.value / float(other.value)
#         except ValueError:
#             print("Value error")
#
#
#
# x = Fraction(1/2)
# y = Fraction(1/4)
#
# print(x+y)
