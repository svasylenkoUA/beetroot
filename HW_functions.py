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