import argparse
import os

if __name__ == '__main__':

    def get_name(arr, uname, passw):
        try:
            lst = arr[uname]
            if uname==lst[1] and passw==lst[2]:
                return lst[0]
            else:
                return "No such user"
        except IndexError:
            return ("No such user")

    os.chdir("cache")

    f = open("test.txt", encoding="utf8")
    d = {}
    for x in f:
        #    print(x.split(";"))
        lst = x.rstrip().split(";")
        d[lst[1]] = lst
    #print(d)

    inp_n = input("Your login:")
    inp_pass = input("Your pass:")

    if get_name(d, inp_n,inp_pass) == "No such user":
        rr = input("No such user, shall we add? (Y, N)")
        if rr == "Y":
            nm = input("Provide: Name;username;pass")
            lst = nm.rstrip().split(";")
            d[lst[1]] = lst
            print(f'Hi {get_name(d, lst[1], lst[2])}')

    else:
        print(f'Hi {get_name(d, inp_n, inp_pass)}')

    f.close()