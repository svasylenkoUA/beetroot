import random
# Task 1
lst=[]
i,x, mx = 0,0, 0
while i<10:
    lst.append(random.randint(1, 100))
    i +=1

while x<len(lst):
    if int(lst[x]) > mx: mx = int(lst[x])
    x +=1

print(lst)
print(mx)

#Task 2
lst1=[]
lst2 = []
res_lst=[]
i,x, mx, cnt, dst = 0,0,0,1,0

while i<10:
    lst1.append(random.randint(1, 10))
    lst2.append(random.randint(1, 10))
    i +=1

while x<10:
    if lst2.count(lst1[x])>0: res_lst.append(lst2[x])
    if lst1.count(lst2[x]) > 0: res_lst.append(lst1[x])
    x +=1

while True:
    cnt = 0
    mx = 0
    dst = len(res_lst)
    while mx<dst:
        cc = res_lst[mx]
        dd = res_lst.count(res_lst[mx])
        if res_lst.count(res_lst[mx])>1:

            res_lst.pop(mx)
            cnt +=1
        dst = len(res_lst)
        mx += 1

    if cnt == 0: break

print(lst1)
print(lst2)
print(res_lst)

#Task 3
i=0
lst=[]
res_lst=[]

lst = list(range(1,101))

while i<len(lst):
    if lst[i] % 7 == 0 and lst[i] % 5 != 0:
        res_lst.append(i)
    i+=1

print(res_lst)