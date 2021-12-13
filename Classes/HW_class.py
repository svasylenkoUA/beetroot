class Person:

    def __init__(self, firstname="", lastname="", age=0):
        self.fname = firstname
        self.lname = lastname
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.fname} {self.lname} and I’m {self.age} years old')


person1 = Person("Carl", "Johnson", 26)
person1.talk()

class Dog:
    age_factor = 7

    def __init__(self, age=0):
        self.age = age

    def human_age(self, equv=0):
        return equv*self.age_factor

dog1 = Dog()
print(dog1.human_age(10))

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:

    def __init__(self, ch_list):
        self.channels = ch_list
        self.curr_channel=0

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[-1]

    def turn_channel(self, numb):
        try:
            self.curr_channel = numb-1
            return self.channels[numb-1]
        except IndexError:
            return "No such channel"

    def next_channel(self):
        if self.curr_channel + 1 >= len(self.channels):
            self.curr_channel=0
            return self.channels[0]
        else:
            self.curr_channel +=1
            return self.channels[self.curr_channel]

    def prev_channel(self):
        if self.curr_channel - 1 < 0:
            self.curr_channel=len(self.channels)-1
            return self.channels[self.curr_channel]
        else:
            self.curr_channel -=1
            return self.channels[self.curr_channel]

    def current_channel(self):
        return self.channels[self.curr_channel-1]

    def is_exist(self, param):
        if type(param) == int:
            if 0<=param<=len(self.channels)-1:
                return "Yes"
            else: return "No"
        elif type(param) == str:
            if param in set(self.channels):
                return "Yes"
            else: return "No"
        else:
            return "No"


controller = TVController(CHANNELS)
print(controller.channels)
print(controller.first_channel())
print(controller.last_channel())
print("--")
print(controller.turn_channel(2))
print(controller.next_channel())
print(controller.next_channel())
print(controller.next_channel())
print("--")
print(controller.prev_channel())
print(controller.prev_channel())
# print(controller.prev_channel())
print("--")
print(controller.is_exist(2))
print(controller.is_exist("BBC"))
print(controller.is_exist("CNN"))
print(controller.is_exist(5))

class Friend:

    def __init__(self, name, phone=""):
        self.name = name
        self.phone = phone

u1 = Friend("Андрей", "+380331233333")
u2 = Friend("Петр", )

assert hasattr(u1, "name")
assert hasattr(u1, "phone")
assert u1.name == "Андрей"
assert u2.name == "Петр"
assert u1.phone == "+380331233333"
assert u2.phone == ""


class SymbolA:
    def __init__(self, sign):
        self.sign = sign

    def line(self, numb=0):
        if numb == 0:
            return " " + self.sign+self.sign+self.sign
        elif numb == 1 or numb == 3:
            return self.sign + "  " + self.sign
        elif numb == 2:
            return self.sign+self.sign+self.sign+self.sign
        else:
            return ""

a = SymbolA('@')
assert a.line(0) == " @@@"
assert a.line(1) == "@  @"
assert a.line(2) == "@@@@"
assert a.line(3) == "@  @"

a2 = SymbolA('$')
assert a2.line(0) == " $$$"
assert a2.line(1) == "$  $"
assert a2.line(2) == "$$$$"
assert a2.line(3) == "$  $"



class SymbolA:
    def __init__(self, sign):
        self.sign = sign
        self.called_times = 0

    def line(self):
        self.called_times += 1
        if self.called_times > 4:
            raise StopIteration

        if self.called_times == 1:
            return " " + self.sign+self.sign+self.sign
        elif self.called_times == 2 or self.called_times == 4:
            return self.sign + "  " + self.sign
        elif self.called_times == 3:
            return self.sign+self.sign+self.sign+self.sign
        else:
            return ""


a = SymbolA('@')
b = SymbolA('@')

assert a.line() == " @@@"
assert a.line() == "@  @"
assert b.line() == " @@@"
assert a.line() == "@@@@"
assert a.line() == "@  @"
assert b.line() == "@  @"
try:
    a.line()
    assert False, "Исключение не брошено!"
except StopIteration:
    assert True, "Все правильно сделал!"
except:
    assert False, "Ну я же просил StopIteration кидать а не что попало."