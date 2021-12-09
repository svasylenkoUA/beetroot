class Person:

    def __init__(self, firstname="", lastname="", age=0):
        self.fname = firstname
        self.lname = lastname
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.fname} {self.lname} and I’m {self.age} years old')


person1 = Person("Carl", "Johnson", 26)
person1.talk()

# Create a class Dog with class attribute `age_factor` equals to 7.
# Make __init__() which takes values for a dog’s age. Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, age=0):
        self.age = age

    def human_age(self, equv=0):
        return equv*self.age_factor

dog1 = Dog()
print(dog1.human_age(10))