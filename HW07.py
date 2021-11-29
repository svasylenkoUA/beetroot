#Make a program that has some sentence (a string) on input
#and returns a dict containing all unique words as keys and the number of occurrences as values.


if __name__ == '__main__':

    def dd(item):
        if item in dct:
            cnt = dct[item]+1
            dct.update({item:cnt})
        else:
            dct[item] = 1

    inp = "Это рандомная строка состоящая из слов содержит рандомная количество слов"
    inp = inp.split(" ")
    dct = dict()

    for i in inp:
        dd(i)

    for key, value in dct.items():
        print(key,":", value)

    #Task 2

    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }

    def ttl_price(dct1, dct2):
        res = 0
        for key, value in dct1.items():
            if key in dct2.keys():
                res = res + dct2[key]*value

        return res

    #Task 3

    print(ttl_price(stock,prices))

    lst = [tuple((i, i**2)) for i in range(1,11,1)]
    print(lst)

