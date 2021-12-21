# def logger(func):
#     def wrapper(*args):
#         return f'{func.__name__} is called with arguments {args}'
#     return wrapper
#
#
# @logger
# def add(x, y):
#     return x + y
#
# @logger
# def square_all(*args):
#     return [arg ** 2 for arg in args]
#
#
# print(add(4,5))

# def stop_words(words: list):
#     def decorator(func):
#         def wrapper(name):
#             rr = func(name)
#             for i in words:
#                 rr = rr.replace(str(i), '*')
#             return rr
#         return wrapper
#     return decorator
#
# @stop_words(['pepsi', 'BMW'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"
#
# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(name):
            if type(name) is not type_:
                print("Arg error, type is not string")
                return False
            if len(name)>max_length:
                print("Oversize: >15")
                return False
            result = func(name)
            cont = False
            for i in contains:
                if result.find(i) != -1:
                    cont = True
            if cont:
                return result
            else:
                return False

        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'