# home 1

t = "5142"
a = t[0]
b = t[1]
c = t[2]
d = t[3]
if int(a) + int(b) ==  int(c) + int(d):
    print("Счастливое число")
else:
    print("Не повезло ")


# Home 2

w = input()
if w == w[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")


# home 3


import math
x = float(input("x="))
y = float(input("y="))
r = 4
xyp = math.sqrt(x ** 2 + y ** 2)
if xyp <= r:
    print("Точка попала в круг")
else:
    print("Точка не попала в круг")




# home 4                     #Выводит список нечетных чисел

sp = [1,5,8,9,15,88,4,2]
for i in sp:
    if i % 2:
        print(i)

sp = [1,5,8,9,15,88,4,2]          #Выводит количество  нечетных чисел
count = 0
for i in sp:
    if i % 2:
       count += 1
print(count)


# home 5

l = [2,5,33,21] * 2
for i in range(4,8):
    s[i] *= 2
print(l)


# home 6

import random
zp = []
for i in (range(12)):
    zp.append(random.randint(7500,15000))
print("Суммв ЗП за год: ", zp)
print("********")
print("Средняя ЗП за месяц ", sum(zp) // 12)




# 7 задача

sp = list(range(4))
s1 = sp[0] = [1,2,3,4]
s2 = sp[1] = [5,6,7,8]
s3 = sp[2] = [9,10,11,12]
s4 = sp[3] = [13,14,15,16]
for i in sp:
    print(i)










