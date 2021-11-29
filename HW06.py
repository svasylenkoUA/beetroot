# import random
# # Task 1
# lst=[]
# i,x, mx = 0,0, 0
# while i<10:
#     lst.append(random.randint(1, 100))
#     i +=1
#
# while x<len(lst):
#     if int(lst[x]) > mx: mx = int(lst[x])
#     x +=1
#
# print(lst)
# print(mx)
#
# #Task 2
# lst1=[]
# lst2 = []
# res_lst=[]
# i,x, mx, cnt, dst = 0,0,0,1,0
#
# while i<10:
#     lst1.append(random.randint(1, 10))
#     lst2.append(random.randint(1, 10))
#     i +=1
#
# while x<10:
#     if lst2.count(lst1[x])>0: res_lst.append(lst2[x])
#     if lst1.count(lst2[x]) > 0: res_lst.append(lst1[x])
#     x +=1
#
# while True:
#     cnt = 0
#     mx = 0
#     dst = len(res_lst)
#     while mx<dst:
#         cc = res_lst[mx]
#         dd = res_lst.count(res_lst[mx])
#         if res_lst.count(res_lst[mx])>1:
#
#             res_lst.pop(mx)
#             cnt +=1
#         dst = len(res_lst)
#         mx += 1
#
#     if cnt == 0: break
#
# print(lst1)
# print(lst2)
# print(res_lst)
#
# #Task 3

res_lst = [i for i in range(0, 101,7) if i % 5 !=0]

print(res_lst)

#Additional tasks
# if __name__ == '__main__':
#
#     import random
#
#     # i = mx = mn = 0
#     # l=[]
#     # while i<10:
#     #     l.append(random.randint(1,100))
#     #     i +=1
#     #
#     # i=0
#     # mn = l[0]
#     # while i<len(l):
#     #     if l[i]>mx: mx = l[i]
#     #     if l[i] < mn: mn = l[i]
#     #     i +=1
#     #
#     # print(l)
#     # print(f'Min: {mn}, max: {mx}')
#     #
#     # # task 2
#     # exmpl = "Привіт"
#     # rr=''
#     # var1 = tuple((exmpl))
#     # var1 = var1[::2]
#     # var1 = ''.join(var1)
#     #
#     # assert var1 == "Пиі"
#     #
#     # #task 3
#     # ans = ''
#     # l=[]
#     # while ans != 'Q':
#     #     ans = input("Enter name: ")
#     #     if ans == 'Q': break
#     #     l.append(ans)
#     #
#     # l.sort()
#     # print(l)
#     # print(f"{l[0]} играет с {l[len(l)-1]}")
#     # print(f"{l[1]} играет с {l[len(l) - 2]}")
#     l=[]
#     for i in range(0,10,1):
#         l.append(i)
#     print(l)
#     i=0
#     while i<len(l)//2:
#         l[i], l[len(l)-i-1] = l[len(l)-i-1], l[i]
#         i+=1
#
#     print (l)
#
