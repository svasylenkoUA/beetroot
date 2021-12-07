# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except state­ment to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?


if __name__ == '__main__':

    # def oops(data):
    #     try:
    #         return data[2]
    #     except IndexError:
    #         print("Index error")
    #
    #
    # dd = [1,2]
    #
    # print(oops(dd))

    def squared():
        try:
            a = int(input("Number1 please:"))
            b = int(input("Number2 please:"))
            return a*a/b
        except ValueError:
            print("Type error")
        except ZeroDivisionError:
            print("B could not be zero")

    print(squared())
