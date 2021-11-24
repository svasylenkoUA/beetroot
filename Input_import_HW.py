import random

quiz = random.randint(1,10)
ans = ''

while True:
    ans = input("Guess the number: ")
    if ans.lower() =='q': break
    if int(ans) == quiz:
        print ("You won!")
        break



#Task 2
name = input("Enter name: ")
age = int(input("Enter age: "))

print("Hello %s, on your next birthday you’ll be %d years" % (name, age+1))

#Task 3
base_str = input("Input string: ")
lst = list(base_str)
i = 0
while i<5:
    random.shuffle(lst)
    print(''.join(lst))
    i += 1



#Task 4
quiz = int(input("What is 2x2? "))
ans = ''

while True:
    ans = input("Nope, once more: ")
    if ans.lower() =='q': break
    if int(ans) == 4:
        print ("You won!")
        break