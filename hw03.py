# task1

a = input("Enter string:")

if len(a) <= 1:
    print("Empty string")
elif len(a)==2:
    print(a+a)
else:
    print(a[:2]+a[-2:])

#Task 2
# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.

a = input("Enter string:")

if a[0] == '+' and a[1:].isnumeric() and len(a[1:])==10:
    print("Number is valid")
else:
    print("Number is not valid")


# Task3
# Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
# The program should check if your input is equal to the stored name even if the given name has another case,
# e.g., if your input is “Anton” and the stored name is “anton”, it should return True.

nm = 'serhii'
ans = input("Enter name: ")

if ans == nm.capitalize(): print("True")