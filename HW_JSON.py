# with open("testfile.txt", "w+") as test:
#     test.write("Hello world\n")
#
# with open("testfile.txt", "r+") as test1:
#     print(test1.read())


import json
import pprint

def search_by(data, field=""):
    arr = []
    def rec_extract(data, arr, field):
        if isinstance(data, dict):
            for k,v in data.items():
                if isinstance(v, (dict, list)):
                    rec_extract(v, arr, field)
                elif k == field:
                    arr.append(v)
        elif isinstance(data, list):
            for item in data:
                rec_extract(item, arr, field)
        return arr

    values = rec_extract(data, arr, field)
    return values


def add_entry(data, new_item):
    data["people"].append({new_item})
    data["numberOfContact"] += 1
    return data

def delete_entry(data, item):
    i = 0
    m = 0
    for d in data["people"]:
        for k,v in d.items():
            if v == item: m = 1
        data["people"].pop(i)
        i +=1
    data["numberOfContact"] -= 1
    return data

def update_entry(data, inp1, inp2):
    i = 0
    m = 0
    for d in data["people"]:
        for k, v in d.items():
            if k == inp1: d[k] = inp2

    return data

while True:
    inp = input("Would you like to: S - search, A - add, U - update, D - delete:")

    with open("phonebook.txt", "r+") as book:
        data = json.load(book)

    if inp == "S":
        inp1 = input("Search element: ")
        print(search_by(data, inp1))
    elif inp =="A":
        inp1 = input("Add data element: ")
        pprint.pprint(add_entry(data, inp1))
    elif inp == "U":
        inp1 = input("Update data element: ")
        inp2 = input("Update data element to: ")
        pprint.pprint(update_entry(data, inp1, inp2))
    else:
        inp1 = input("Delete data element (name): ")
        pprint.pprint(delete_entry(data, inp1))