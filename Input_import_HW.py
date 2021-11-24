#import random
#import itertools
#
# quiz = random.randint(1,10)
# ans = ''
#
# while True:
#     ans = input("Guess the number: ")
#     if ans.lower() =='q': break
#     if int(ans) == quiz:
#         print ("You won!")
#         break
#
#
#
# #Task 2
# name = input("Enter name: ")
# age = int(input("Enter age: "))
#
# print("Hello %s, on your next birthday you’ll be %d years" % (name, age+1))
#
# #Task 3
# base_str = input("Input string: ")
# lst = list(base_str)
# i = 0
# while i<5:
#     random.shuffle(lst)
#     print(''.join(lst))
#     i += 1
#
#
#
# #Task 4
# quiz = int(input("What is 2x2? "))
# ans = ''
#
# while True:
#     ans = input("Nope, once more: ")
#     if ans.lower() =='q': break
#     if int(ans) == 4:
#         print ("You won!")
#         break
#
#

# Additional task #1

# while True:
#     x = random.randint(1,30)
#     f = random.randint(0,2)
#     if f ==0:
#         y = 2*x+3
#     elif f == 1:
#         y = 3*x+15
#     else: y = x+7
#
#     flist = ['y=2x+3','y=3x+15','y=x+7']
#
#     print(flist[f])
#     print('x = ', x)
#
#     res = input("y = ?:")
#
#     if res.isnumeric():
#         if int(res) == y:
#             print ("Молодец")
#             break
#
#     if res == 'q':
#         break
#
#     print("Ты можешь лучше\n")

# Additional task #2

import itertools
r = 0
ans = ''

while r != 1:
    ans = input("String: ")
    if len(ans) > 5:
        r = 1
        break

    print("String must be 5+ letters")

rr = itertools.combinations(ans,5)
y = 0
for x in rr:
    if y>4: break
    print(''.join(x))
    y +=1