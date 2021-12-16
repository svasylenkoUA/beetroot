class Person:
    def __init__(self, name):
        self.name = name
        self.init_setup()

    def init_setup(self):
        pass

class Boss(Person):

    def init_setup(self):
        self.employed_people = []


    def employ(self, employee: "Employee"):
        if not employee.boss:
            self.employed_people.append(employee)
            employee.employed(self)
        else:
            print(employee.name + " already has boss")

    def resign(self, employee: "Employee"):
        if employee in self.employed_people:
            print(employee.name + " я тебя увольняю!!!")
            self.employed_people.remove(employee)
            employee.resigned()
        else:
            print(employee.name + " is not your employee")

    def whom_I_have(self):
        return [str(x) for x in self.employed_people]

    def __str__(self):
        return "I am cool boss and my name is " + self.name + " and I have " + str(len(self.employed_people)) + " employees"

class Employee(Person):

    def init_setup(self):
        self.boss = None

    def where_I_am(self):
        return f'I work for {self.boss.name}'

    def resigned(self):

        if self.boss:
            self.boss.resign(self)
            self.boss = None
            print("I am " + self.name + ". Квасим, меня уволили")

    def employed(self, boss: Boss):
        self.boss = boss
        print("I am " + self.name + ". Квасим, нашел работу")

    def __repr__(self):
        if self.boss:
            return "I am " + self.name + " and work for " + self.boss.name
        else:
            return "I am " + self.name + " and I am crypro-guru"

b1 = Boss("Миша")
b2 = Boss("Юра")
e1 = Employee("Гриша")
e2 = Employee("Опанас")

e1.resigned()

print(b1)
print(b2)
print(e1)
print(e2)


b1.employ(e1)
b2.employ(e1)
b2.employ(e2)
print(b1.whom_I_have())
e1.resigned()
print("------")
print(b1.whom_I_have())