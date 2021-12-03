# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
# The function should then print “My favorite movie is named {name}”.


def favorite_movie(name):
    print(f"My favorite movie is named {name}")

favorite_movie('Thor')

# Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
# Make the function print out the values of the dictionary to make sure that it works as intended.


def make_country(name, capital):
    dct = {name:capital}
    for i in dct.keys():
        print(i, " : ", dct[i])

make_country("Ukraine", "Kyiv")

# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
# and an arbitrary number of arguments (only numbers) as the second parameter.
# Then return the sum or product of all the numbers in the arbitrary parameter.

# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42

def make_operation(oper, *args):
    res = 0

    if oper == "+":
        for i in range(0, len(args)):
           res += args[i]
    if oper == "-":
        for i in range(0, len(args)):
            res -= args[i]
    if oper == "*":
        res = 1
        for i in range(0, len(args)):
            res = res * args[i]
    return res

assert make_operation("+", 7, 7, 2) == 16
assert make_operation("-", 5, 5, -10, -20) == 20
assert make_operation("*", 7, 6) == 42


#Напишите функцию которая будет переводить возраст с Земного на Марсианский. В году на Земле 365 дней а на марсе 687

def mars_age(age: int) -> int:
    return age*365//687


assert mars_age(10) == 5
assert mars_age(63) == 33
assert mars_age(1000) == 531

#Напишите функцию greet принимающую имя name (type:str) м слово word (type:str). Если слово не передано то считать его " -" и возвращающую строку вида "[Имя] ты сегодня [слово]!"

def greet(name, word="-"):

    return name.capitalize() + " ты сегодня " + word +"!"

assert greet("111", "2") == "111 ты сегодня 2!"
assert greet("игорь", "молодец") == "Игорь ты сегодня молодец!"
assert greet(name="ольга", word="супер") == "Ольга ты сегодня супер!"
assert greet("николай") == "Николай ты сегодня -!"


#Напишите функцию joinA которая принимает неограниченное количество значений любого типа и возвращает строку где эти значения склеены через символ A

#Попробуйте написать с помощью компрехеншена одной строкой return ___magic___

def joinA(*args):
    return 'A'.join([str(i) for i in args])

assert joinA("Привет", "мир", "!") == "ПриветAмирA!"
assert joinA("Привет", 1, 2, 3, True) == "ПриветA1A2A3ATrue"
assert joinA() == ""

# 21
import random

def get_deck() -> list[dict]:
    '''Возвращает лист карт'''
    pass

def shuffle_deck(deck: list[dict]) -> list[dict]:
    for i in range(1,14):
        p1, p2 = random.randint(0,12), random.randint(0,12)
        deck[p1], deck[p2] = deck[p2], deck[p1]
    return deck

def calculate(hand: list[dict]) -> int:
    i=res=0
    while i<len(hand):
        res += hand[i]
        i +=1
    return res

def want_more() -> bool:
    return his_deck.append(deck.pop(0))



deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]
his_deck = []
my_deck = []
my_bank = 0
shuffle_deck(deck)

while True:
    while input("Want more? ") == "Y":
        want_more()

    if calculate(his_deck)>21:
        print("His deck", his_deck)
        print("Looser!")
        his_deck.clear()
        continue

    while my_bank<15:
        my_bank += deck[0]
        my_deck.append(deck.pop(0))

    print("My deck", my_deck)
    print("His deck", his_deck)

    if calculate(my_deck)>21 or calculate(his_deck) > calculate(my_deck):
        print("You win!")
    elif calculate(his_deck) == calculate(my_deck):
        print("Ups, one more time")
    else: print("I win!")