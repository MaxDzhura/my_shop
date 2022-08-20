# Создайте класс «Прямоугольник», у которого присутствуют два поля
# (ширина и высота). Реализуйте метод сравнения прямоугольников по
# pлощади. Также реализуйте методы сложения прямоугольников (площадь
# суммарного прямоугольника должна быть равна сумме площадей
# прямоугольников, которые вы складываете). Реализуйте методы
# умножения прямоугольника на число n (это должно увеличить площадь
# базового прямоугольника в n раз).


n = int(input("Введите любое число :"))

class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):                                      #Метод --Сравнение-- "=="
        return self.a * self.b == other.a * other.b

    def __add__(self, other):                                      #Метод --Сложение-- "+"
        return Rectangle(self.a + other.a , self.b + other.b)


    def __mul__(self, other):                                    #Метод --Умножение-- "*"
        return Rectangle(self.a * other ,self.b * other)


    def __str__(self):
        return f"{self.a}--{self.b}"

r1 = Rectangle(2,4)
r2 = Rectangle(2,3)
r3 = Rectangle(2,4)
r4 = Rectangle(2,4)
q = r1 + r2 + r3 + r4

print(q)

s = r1 * n
print(s)

