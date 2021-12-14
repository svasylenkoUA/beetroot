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
    def __init__(self):
        pass

    def new_book(self):
        pass
    def group_by_author(self):
        pass
    def group_by_year(self):
        pass

class Book(Author):
    def __init__(self, name, year, author):
        super().__init__(name, country, birthday):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return self.name + " " + self.author.name + " " + self.year

    def __str__(self):
        self.__repr__()

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