#Create your own implementation of a built-in function enumerate, named `with_index`, which takes two
# parameters: `iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function

# def with_index(iterable=[], start=0):
#     cnt = 0
#     for i in iterable:
#         if cnt >= start and cnt<len(iterable):
#             yield cnt, i
#         elif cnt>=len(iterable)+1:
#             raise StopIteration
#         else:
#             pass
#         cnt +=1
#
# for m in with_index([1,2,3,4,5,6,7,8,9], 4):
#     print(m)

#Create your own implementation of a built-in function range, named in_range(), which takes three
# parameters: `start`, `end`, and optional step. Tips: See the documentation for `range` function

def in_range(start=0, end=0, step=1):
    cnt = start
    if step>0:
        while cnt <= end:
            yield cnt
            cnt += step
    else:
        while cnt >= end:
            yield cnt
            cnt += step

for m in in_range(11,2, -2):
    print(m)
