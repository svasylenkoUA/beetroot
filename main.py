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