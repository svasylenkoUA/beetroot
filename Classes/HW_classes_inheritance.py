# class Person:
#
#     def __init__(self, name, surname, gender, age):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.age = age
#
# class Student(Person):
#
#     def __init__(self, name, surname, gender, age, school, pclass):
#         super().__init__(name, surname, gender, age)
#         self.school = school
#         self.pclass = pclass
#
#
# class Teacher(Person):
#
#     def __init__(self, name, surname, gender, age, salary, title):
#         super().__init__(name, surname, gender, age)
#         self.salary = salary
#         self.title = title
#
#     def __repr__(self):
#         return (self.surname + " " +self.name + ": " + self.title + ", " + str(self.age))
#
# t1 = Teacher("John", "Smith", "M", 40, 25000, "Head of Math")
#
# print(t1)
#
# class Mathematician:
#
#     def __init__(self):
#         pass
#
#     def square_nums(self, lst):
#         return [x*x for x in lst]
#
#     def remove_positives(self, lst):
#         return [x for x in lst if x < 0]
#
#     def filter_leaps(self, lst):
#         return [x for x in lst if x % 4 == 0]
#
# m = Mathematician()
#
# assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
# assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
# assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
#
#
# class CustomException(Exception):
#
#     def __init__(self, msg):
#         f = open("log.txt", 'a')
#         f.write(msg)
#         f.close()


class Product:
    def __init__(self, ptype, pname, or_price):
        self.ptype = ptype
        self.pname = pname
        self.price = or_price
        self.full_price = 0

class Margin:
    def __init__(self):
        self.rules = {
            "Sport": 20,
            "Food": 10
        }

    def calc_full_price(self, prod: Product):
        return prod.price*(1 + self.rules[prod.ptype]/100)



class ProductsInShop(Product):
    def __init__(self, prod: Product):
        self.product = prod
        m = Margin()
        prod.full_price = m.calc_full_price(prod)
        self.quantity = 0


class ProductStore:
    MARGIN = 10

    def __init__(self):
        self.items_in_store = []

    def add(self, product, quantity):
        p = ProductsInShop(product)
        p.quantity = quantity
        self.items_in_store.append(p)

    def sell(self, product, quantity):
        for i in self.items_in_store:
            if i.product.pname == product:
                i.quantity -= quantity
            else:
                continue


    def get_income(self):
        income = 0
        for p in self.items_in_store:
            income += (p.product.full_price - p.product.price)*p.quantity
        return income

    def get_all_items(self):
        return [p.product.pname+str(p.quantity) for p in self.items_in_store]


p1 = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Chicken', 80)

ps1 = ProductStore()

ps1.add(p1, 20)
ps1.add(p2, 10)
print(ps1.get_all_items())
print(ps1.get_income())
ps1.sell("Chicken", 5)
print(ps1.get_all_items())
print(ps1.get_income())
