# import re
#
# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#
# class Email_val:
#
#     @classmethod
#     def validate(cls, email):
#         if (re.fullmatch(regex, email)):
#             print("Valid Email")
#         else:
#             print("Invalid Email")
#
# e = Email_val
# email = "ankitrai326@gmail.com"
# e.validate(email)
# email = "my.ownsite@our-earth.org"
# e.validate(email)
# email = "ankitrai326.com"
# e.validate(email)

# class Boss:
#
#     def __init__(self, id_: int, name: str, company: str):
#         self.id = id_
#         self.name = name
#         self.company = company
#         self.workers = []
#
#     @property
#     def employ(self):
#         return f'I have {str(len(self.workers))} employees'
#
#     @employ.setter
#     def employ(self, employee: "Worker"):
#         if not employee.boss:
#             self.workers.append(employee)
#             Worker.my_boss = self
#             return f'{employee.name} employed'
#         else:
#             return f'{employee.name} already has a boss'
#
#     @employ.deleter
#     def employ(self, employee: "Worker"):
#         if employee.boss:
#             self.workers.remove(employee)
#             del Worker.my_boss
#         else:
#             return f'{employee.name} is not my employee'
#
#     def __repr__(self):
#         return f'I am boss: {self.name}, my company called {self.company} and I have {str(len(self.workers))} employees'
#
#
# class Worker:
#
#     def __init__(self, id_: int, name: str, boss: Boss, company=None):
#         self.id = id_
#         self.name = name
#         self.company = company
#         self.boss = boss
#
#     @property
#     def my_boss(self):
#         if self.boss:
#             return self.boss.name
#         else:
#             return f'No boss at the moment'
#
#
#     @my_boss.setter
#     def my_boss(self, boss: Boss):
#         self.boss = boss
#         self.company = boss.company
#         return('Boss was set')
#
#     @my_boss.deleter
#     def my_boss(self):
#         self.boss = None
#         self.company = None
#         return('Boss deleted')
#
#
#     def __str__(self):
#         if self.boss:
#             return f'My name is {self.name} and I work for {self.boss.name} in company {self.company}'
#         else:
#             return f'I am {self.name} and jobless'
#
# w1 = Worker(1, 'Kolya', None, None)
# w2 = Worker(2, 'Misha', None, None)
# w3 = Worker(3, 'Petya', None, None)
#
# b1 = Boss(1, 'Mykola Petrovych', 'Wow')
# b2 = Boss(2, 'Svyryd Opanasovych', 'Yoy')
#
# print(w1)
# print(w1.my_boss)
# w1.my_boss = b1
# print(w1.my_boss)
# print(w1)
# del w1.my_boss
# print(w1)




# class TypeDecorators:
#
#     @TypeDecorators
#     def get_var(self):
#         pass
#
#     def to_int(self, var):
#         return int(var)
#
#     def to_str(self, var):
#         return str(var)
#
#     def to_bool(self, var):
#         return bool(var)
#
#     def to_float(self, var):
#         return float(var)
#
# @TypeDecorators.to_int
# def do_nothing(string: str):
#     return string

#
# @TypeDecorators.to_bool
# def do_something(string: str):
#     return string
#
# print(do_nothing("25"))

#assert do_nothing('25') == 25

#assert do_something('True') is True

# class Brezaolla():
#     def_meat = 600
#     def_wine = 500
#     def_olive_oil = 100
#     def_chabrets = 2
#     def_leaf = 2
#     def_petr = 1
#     def_ukrop = 1
#     def_basil = 1
#     def_salt = 18
#
#     def __init__(self, weight_of: int = 600):
#         self.meat = weight_of
#         self.wine = self.propor(self.def_wine, weight_of, self.def_meat)
#         self.olive_oil = self.propor(self.def_olive_oil, weight_of, self.def_meat)
#         self.chabrets = self.propor(self.def_chabrets, weight_of, self.def_meat)
#         self.leaf = self.propor(self.def_leaf, weight_of, self.def_meat)
#         self.petr = self.propor(self.def_petr, weight_of, self.def_meat)
#         self.ukrop = self.propor(self.def_ukrop, weight_of, self.def_meat)
#         self.basil = self.propor(self.def_basil, weight_of, self.def_meat)
#         self.nitrit = self.propor(self.def_salt, weight_of, self.def_meat)
#         self._weight = self.meat + self.wine + self.olive_oil + self.chabrets + self.leaf + self.petr + self.ukrop + self.basil + self.nitrit
#
#
#     @staticmethod
#     def propor(ingrid, meat_w, def_meat):
#         return meat_w*ingrid/def_meat
#
#     @property
#     def weight(self):
#         return self._weight
#
#     def set_weight(self, num):
#         self._weight = num
#
#
# r1 = Brezaolla(600)
# r2 = Brezaolla(1200)
#
# assert r1.wine == 500
# assert r2.wine == 1000
# assert r1.nitrit == 18
# assert r2.nitrit == 36
#
# assert r2.weight == 2450
# try:
#     r2.weight=1000
#     assert False, 'Должно быть нельзя менять вес напрямую'
# except AttributeError:
#     pass
#
#
# r1.set_weight(1000)
# assert r1.weight == 1000

import functools

class TypeDecorators:

    def mydeco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

        return wrapper




@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25

assert do_something('True') is True

