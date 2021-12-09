# class Person:
#
#     def __init__(self, firstname="", lastname="", age=0):
#         self.fname = firstname
#         self.lname = lastname
#         self.age = age
#
#     def talk(self):
#         print(f'Hello, my name is {self.fname} {self.lname} and I’m {self.age} years old')
#
#
# person1 = Person("Carl", "Johnson", 26)
# person1.talk()
#
# class Dog:
#     age_factor = 7
#
#     def __init__(self, age=0):
#         self.age = age
#
#     def human_age(self, equv=0):
#         return equv*self.age_factor
#
# dog1 = Dog()
# print(dog1.human_age(10))

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    curr_channel = 0
    def __init__(self, ch_list):
        self.channels = ch_list

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
print(controller.is_exist(5))
print(controller.is_exist("CNN"))
