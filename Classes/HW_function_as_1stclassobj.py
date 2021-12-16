#task 1
def some_function():
    a = 8
    string_var= "some_string"

print(some_function.__code__.co_nlocals)

#task 2
#Write a Python program to access a function inside a function (Tips: use function, which returns another function)


def first_function(x):
    def second_function(y):
        return x+y
    return second_function

res = first_function(5)
print(res(10))

#task 3

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums, func1, func2):
    if len([n for n in nums if n < 0]) == 0:
        return func1(nums)
    else:
        return func2(nums)

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]