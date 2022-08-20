# home 1


s = int(input())
sp = {1:"понедельник",2:"вторник",3:"среда",4:"четверг",5:"пятница",6:"суббота",7:"воскресение"}
if s == 1:
    print(sp.get(1))
elif s == 2:
    print(sp.get(2))
elif s == 3:
    print(sp.get(3))
elif s == 4:
    print(sp.get(4))
elif s == 5:
    print(sp.get(5))
elif s == 6:
    print(sp.get(6))
elif s == 7:
    print(sp.get(7))
else:
    print("Не верный ввод")


# home 2

cat = {"Имя": "Кузя", "Возраст": 4, "Цвет": "Серый", "Пол": "Мужской", "Вес": 3900 }
print(cat)

# home 3


p = input().replace(" ", "")
sl = {}
for i in p:
    if sl.get(i):
        sl[i] += 1
    else:
        sl[i] = 1
print(sl)



# римские цифры:


R = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s = input("Введите римское число :")
posl = s[-1]
res = R[posl]
for i in s[-2::-1]:
	if R[i] >= R[posl]:
		res += R[i]
	else:
		res -= R[i]
	posl = i
print(res)
