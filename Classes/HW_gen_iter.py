#Create your own implementation of a built-in function enumerate, named `with_index`, which takes two
# parameters: `iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function


def with_index(iterable=[], start=0):
    cnt = 0
    for i in iterable:
        if cnt >= start and cnt<len(iterable):
            yield cnt, i
        elif cnt>=len(iterable)+1:
            raise StopIteration
        else:
            pass
        cnt +=1

for m in with_index([1,2,3,4,5,6,7,8,9], 4):
    print(m)

