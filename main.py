import random

# task 1
total = 44
rez = int(round(44 * 0.8,0))
print ("Task1")
print("Для успешного окончания курса надо сдать {} домашек".format(rez))
assert rez == 35

# task 2
x1 = round(random.random(),2)
x2 = round(random.random(),2)

y1 = round(random.random(),2)
y2 = round(random.random(),2)

dist = round(((x2 - x1)**2 + (y2 - y1)**2)**0.5,4)
print ("Task2")
print("A:", x1, y1, "B is:", x2,y2,"\t", "Distance is:", dist)

# task 3
width = round(random.random(),2)*100
height = round(random.random(),2)*100
depth = round(random.random(),2)*100
diag_sq = round(depth*(width**2 + height**2)**0.5,3)
if diag_sq%12 == 0:
    needed = diag_sq/12
else:
    needed = diag_sq //12 + 1

print("Task 3")

print("Width:", width, "Height is:", height, "Depth is:", depth,  sep="  ")
print("Diag_sq:", diag_sq, "Needed:", needed, "Price is:", needed*600, "Remains m2:", diag_sq%12 , sep="  ")

#task 4
print("\nTask 4")
var1 = 'pyThoN'
var1 = var1.lower().capitalize()
assert var1 == 'Python'

var1 = var1.upper()
assert var1 == 'PYTHON'

var1 = var1.lower()
assert var1 == 'python'

var1 = " python "

var1 = var1.strip()
assert var1 == 'python'

# Task 5
print("\nTask 5")
name = "Остап"
print("Привет, %s " % name)
print("Привет, {}".format(name))
print(f'Привет, {name}')

# Task 6
print("\nTask 6")
price = 12
weight = 3.4121
rez = 0
rez = "Итого: {}".format(round(price*weight,2))
print(rez)
assert rez == 'Итого: 40.95'

# Task 7
print("\nTask 7")
number = 12
username = "ираклий"
access_mask = 54
hour_price=15.321
rez = 0

rez = '0000' + str(number) + ' ' + username.capitalize() + ' ' + str(bin(54)).lstrip('0b') + ' ' + str(round(hour_price,2))
print(rez)
assert  rez == '000012 Ираклий 110110 15.32'

# Task 8
print("\nTask 8")
base_str = 'Корова'
rez = 0
rez = (base_str[4] + base_str[1:4] + 'н' + base_str[5:]).capitalize()
print(rez)
assert rez == 'Ворона'

# Task 9
print("\nTask 9")
a = 10
b = 55
a, b = b, a
assert a==55 and b==10, "Не поменялось. :("
