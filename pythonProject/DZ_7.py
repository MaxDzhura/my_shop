# home 1

s = "bodsfsdb dffd3ghbb dsfbxn  bvvtvb"
print(s.count("b"))


# home 2

v = input("Введите имя: ").title()
if not v.isdigit() and not v.isalpha():
    print("Не верный ввод")
else:
    print(v)


# home 3


t = "Привет"
w = []
for i in t:
    w.append(ord(i))
print(w)
print(sum(w))


# home 4


import math
x = math.pi
print(round(x,2),round(x,3),round(x,4),round(x,5),round(x,6),round(x,7),round(x,8),round(x,9),round(x,10), sep= " *** ")



# home 5

s = input().split()
print(f"Самое длинное слово: {max(s,key=len)}")


