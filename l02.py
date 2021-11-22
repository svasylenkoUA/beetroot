# day_of_week = 5
#
# if day_of_week < 1:
#     print('Ошибка! Дни недели считаются 1-7 ни больше ни меньше!')
# elif day_of_week<6:
#     print('рабочий день')
# elif 6 <= day_of_week <=7:
#     print('выходной')
# else:
#     print('Ошибка! Дни недели считаются 1-7 ни больше ни меньше!')
#
# holiday, day_of_week, wallet = False, 6, 5000
# if wallet<1:
#     print("оно то и можно погулять но не на что")
# elif wallet<100:
#     print("пиво и чипсы на большее денег нет")
# elif wallet<1000:
#     print("гуляем в ресторане, всех угощаю")
# elif wallet>1000:
#     print("После Безоса следующим лечу я. И моя любимая кошка!")
# else:
#     print("работаем")
#
#
# for x in range(101):
#     print(3*x+12)
#
#
# phone = '+380503839699'
# ph, cod, lnght = False, False, False
# a = len(phone)
# if phone.index('+3') == 0: ph = True
# codes = ['050','067','099','063']
# for x in codes:
#     if str(phone[3:6]) == x: cod = True
# if len(phone) == 13: lnght = True
#
# if ph+cod+lnght == 3:
#     print('Phone is valid')
# else:
#     print('Phone is not valid')
#
#
# question = 'Маленькое беленькое на потолко висит не светит'
# answer = 'лампачка'
#
# print(question)
# ans = ''
# while ans.lower() != answer:
#     ans = input('Enter answer:')
#     if ans.lower() == 'q': break
#     if ans.lower() == answer: print('Congrats!')


Задача на колл-центр по-нормальному решается через дерево решений here to be anoter task


# here

# x = int(input("Enter x:"))
# a = int(input("Enter a:"))
#
# b = (x**2 + 4*a**2 + 4*a*x)/(8*a**3)
# y = (2 + x/a)**3/b
#
# v1 = 8*(2*a+x)
# v2 = 8/(x+2*a)
# v3 = (x+2*a)/8
# v4 = 1/(8*(x+2*a))
#
# if y == v1: print("Answer is 1")
# if y == v2: print("Answer is 2")
# if y == v3: print("Answer is 3")
# if y == v4: print("Answer is 4")