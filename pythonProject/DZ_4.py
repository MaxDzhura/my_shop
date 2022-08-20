# Многоквартирный дом
kv = int(input("Введите номер квартиры:"))

if kv <= 36:
    et = (kv - 1) // 4 + 1
    print(f" 1 подъезд, {et} этаж")
elif 36 < kv <= 72:
    et = (kv - 1) // 4 - 8
    print(f" 2 подъезд, {et} этаж")
elif 72 < kv <= 108:
    et = (kv - 1) // 4 - 17
    print(f" 3 подъезд, {et} этаж")
elif 108 < kv <= 144:
    et = (kv - 1) // 4 - 26
    print(f" 4 подъезд, {et} этаж")
else:
    print(f" {kv} : квартиры не существует")


 # Высокосный год

v = int(input("Введите год :"))
if v % 4 and v % 400 and  v % 100 != 0 :
    print(f"{v} - Этот год не высокосный!")
else:
    print(f"{v} - Этот год  высокосный!")


 # Треугольник

a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
if (a + b) > c and (b + c) > a and (a + c) > b:
    print("Треугольник существует")
else:
    print("Треугольника нет")