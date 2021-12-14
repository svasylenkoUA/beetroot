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

    def __init__(self, ptype, pname, price):
        self.ptype = ptype
        self.pname = pname
        self.price = price

class ProductStore:

    def __init__(self):
        self.items_in_store = {}

    def add(self, product, amount):
        try:
            self.items_in_store[product.pname] = amount
        except:
            return "Error adding a product!"

    def set_discount(self, identifier, percent, identifier_type='name'):
        pass

    def sell(self, product_name, amount):
        if self.items_in_store[product_name]<amount:
            raise ValueError("Not enough products available!")
        else:
            self.items_in_store[product_name] -= amount

    def get_income(self):
        pass

    def get_all_products(self):
        pass

    def get_product_info(self, product_name):
        if not product_name in self.items_in_store:
            raise ValueError("No such product")
        else:
            return product_name, self.items_in_store.get(product_name)


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()

s.add(p, 10)
s.add(p2, 300)
s.sell('Ramen', 10)

assert s.get_product_info('Ramen') == ("Ramen", 290)