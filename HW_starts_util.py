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
        except (IndexError, KeyError):
            return ("No such user")


    def add_user(arr):
        nm = input("Provide Name;username;pass: ")
        try:
            lst = nm.rstrip().split(";")
            d[lst[1]] = lst
        except (IndexError, KeyError):
            print("Wrong structure")

    os.chdir("cache")

    f = open("test.txt", encoding="utf8")
    d = {}
    for x in f:
        #    print(x.split(";"))
        lst = x.rstrip().split(";")
        d[lst[1]] = lst
    #print(d)

    parser = argparse.ArgumentParser(description='Add new record')
    parser.add_argument('-record', type=str, help='Name;username;password')

    args = parser.parse_args()

    if args.record != "": add_user(args.record)

    inp_n = input("Your login:")
    inp_pass = input("Your pass:")



    if get_name(d, inp_n,inp_pass) == "No such user":
        rr = input("No such user, shall we add? (Y, N)")
        if rr == "Y":
            add_user(d)
            print(f'Hi {get_name(d, lst[1], lst[2])}')

    else:
        print(f'Hi {get_name(d, inp_n, inp_pass)}')

    f.close()