# домашка 2

a="123"
print(int(a))

b= 123
print(float(b))

c= 12.345
print(int(c))


card = "1234598741256474"
x = card[12:]
print(f"Последние 4 цыфры карты:{x} ")
# Или такой вариант

card = 1234598741256474
c = card % 10000
print(c)



x = int(input("Введите 3-х значное число:"))
print( x // 100 + x // 10 % 10 + x % 10)


a=10
b=12
c=14
p= (a+b+c)/2
s= p*(p-a)*(p-b)*(p-c)
print(s)

# Домашка 3:

x = int(input('введите число: '))
print ((x < 0 and x) or '')

x = int(input())
s = x < 20
print(s)

x = int(input())
s = x == 0
print(s)

d = int(input())
print("Число четное: ", not bool(d % 2 ))


a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
print("Максимальное число: ", max(a,b,c))

   # РАССКАЖИТЕ ПОЧЕМУ НЕ РАБОТАЕТ ЭТОТ ВАРИАНТ
#  x = int(input("Введите числа: "))
#  print("Максимальное число: ", max(x))