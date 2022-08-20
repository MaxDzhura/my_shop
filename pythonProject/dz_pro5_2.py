# Создайте класс «Правильная дробь» и реализуйте методы сравнения,
# сложения, вычитания и произведения для экземпляров этого класса.

class D:

    def __init__(self, a,b):

        self.a = a
        self.b = b

    def __add__(self, other):
        return D(self.a * other.b + other.a * self.b,
                                self.b * other.b)

    def __sub__(self, other):
        return D(self.a * other.b - other.a * self.b,
                               self.b * other.b)

    def __mul__(self, other):
        return D(self.a * other.a, other.b * self.b)

    def __eq__(self, other):
        return self.a / self.b == other.a / other.b

    def __ne__(self, other):
        return self.a / self.b != other.a / other.b

    def __gt__(self, other):
        return self.a / self.b > other.a / other.b

    def __lt__(self, other):
        return self.a / self.b < other.a / other.b

    def __ge__(self, other):
        return self.a / self.b >= other.a / other.b

    def __le__(self, other):
        return self.a / self.b <= other.a / other.b

    def __str__(self):
        return f' {self.a} / {self.b}'


d1 = D(3, 3)
d2 = D(2, 6)

print( d1 + d2)
print( d1 - d2)
print(d1 * d2)
print( d1 == d2)
print(d1, d2)
print( d1 != d2)