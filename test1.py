lst = ["a", 10, "b", 20, "c", 30]

dict = dict(zip(lst[::2], lst[1::2]))
print(dict)