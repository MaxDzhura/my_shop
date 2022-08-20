# 1) Создайте дескриптор, который будет делать поля класса управляемые им
# доступными только для чтения.


class Descriptor:

    def __get__(self, instance, owner):
        return instance.name, instance.age

    def __set__(self, instance, value):
        raise AttributeError()

    def __delete__(self, instance):
        raise AttributeError()


class Cat:

    value = Descriptor()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Cat:  {self.name},  {self.age}"


cat1 = Cat('Bob', 2)
print(cat1)

# ---------------------------------------------2 ВАРИАНТ ОТ ОЛЕГА---------------------------------------------------

class AreaDescriptor:

    def __get__(self, instance, owner):
        p = (instance.x + instance.y + instance.z) / 2
        area = (p * (p - instance.x) * (p - instance.y) * (p - instance.z)) ** 0.5
        return area

    def __set__(self, instance, value):
        raise AttributeError()

    def __delete__(self, instance):
        pass

class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    area = AreaDescriptor()

    def __str__(self):
        return f'{self.x} x {self.y} x {self.z}'

x_1 = Triangle(10,20,15)

print(x_1.area)



# 2) Реализуйте функционал, который будет запрещать установку полей класса
# любыми значениями, кроме целых чисел. Т.е., если тому или иному полю
# попытаться присвоить, например, строку, то должно быть возбужденно
# исключение.


class Figure:


    def __init__(self, height, width, long):
        self.height = height
        self.width = width
        self.long = long

    def __str__(self):
        return f" {self.height}, {self.width}, {self.long}"

    def __setattr__(self, key, value):
        if isinstance(value, int):
            self.__dict__[key] = value
        else:
            raise AttributeError()

fig1 = Figure(10, 10, 20)

print(fig1)


# ---------------------------------------------2 ВАРИАНТ ОТ ОЛЕГА---------------------------------------------------

class Figure:


    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

                                                # __getattribute__ - ВЫЗЫВАЕТСЯ ПРИ ПОПЫТКЕ ПОЛУЧЕНИЯ ЗНАЧЕНИЯ --ЛЮБОГО-- ПОЛЮ КЛАССА
    def __setattr__(self, key, value):          # __getattr__ - ВЫЗЫВАЕТСЯ ПРИ ПОПЫТКЕ ПОЛУЧЕНИЯ ЗНАЧЕНИЯ НЕОПРЕДЕЛЕННОГО ПОЛЮ КЛАССА
        if isinstance(value, (int, float)):    # __setattr__ - ВЫЗЫВАЕТСЯ ПРИ ПОПЫТКЕ ПРИСВОЕНИЯ ЗНАЧЕНИЯ ЛЮБОМУ ПОЛЮ КЛАССА
            self.__dict__[key] = value          # __delattr__ - ВЫЗЫВАЕТСЯ ПРИ УДАЛЕНИИ ПОЛЯ КЛАССА
        else:
            raise AttributeError()


    def __str__(self):
        return f" {self.a}, {self.b}, {self.c}"

fig1 = Figure(10, 10, 20)

print(fig1)



# 3) Реализуйте свойство класса, которое обладает следующим
# функционалом: при установки значения этого свойства в файл с заранее
# определенным названием должно сохранятся время (когда устанавливали
# значение свойства) и установленное значение.


from datetime import datetime

class Town:

    def __init__(self, city, __year):
        self.city = city
        self.__year = __year

    def __str__(self):
        return f" {self.city}, {self.__year}"

    year = property()

    @year.getter
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value
        with open('year.txt', 'a') as f:
            f.write(f' {value}, : {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}\n')


t = Town('Odessa', 2022)
print(t)


# ---------------------------------------------2 ВАРИАНТ ОТ ОЛЕГА---------------------------------------------------


import datetime

class Car:

    def __init__(self, a, b, c):

        self.a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        with open('testfile.txt', 'a', encoding= 'utf-8') as f:
            res_str = f'{datetime.datetime.now()}, {value}\n'
            f.write(res_str)
            self.__a = value



    def  __str__(self):
        return f" {self.a} x {self.__b} x {self.__c}"



car1 = Car('BMW', 19000, 2020)
car1.a = 'honda'
print(car1)



# -----------------------------------------------ЛЕКЦИЯ 13-----------------------------------------

# 1) Создайте ABC класс с абстрактным методом проверки целого числа на
# простоту. Т.е., если параметром этого метода является целое число и оно
# простое, то метод должен вернуть True, а в противном случае False.
# 2) Создайте класс его наследующий.
# 3) Создайте класс, который не наследует пользовательский ABC класс, но
# обладает нужным методом. Зарегистрируйте его в качестве виртуального
# подкласса.
# 4) Проверьте работоспособность проекта.

import abc

class NumberValidatorPrime(abc.ABC):

    @abc.abstractmethod  # 1) класс с абстрактным методом
    def check(self, number):
        if not isinstance(number, int):
            raise TypeError()
        for i in range(1, number):
            if i == 1:
                continue
            for j in range(2, number):
                if not number % j:
                    return False
                else:
                    return True


class SomeClass(NumberValidatorPrime):  # 2) класс наследующий его
    def __init__(self, number):
        self.number = number

    def check(self, number):  # реализовали обязательный метод check в дочернем классе
        return super().check(number)  # теперь можно создать объект этого класса, потому что мы реализовали
    # здесь метод check из абстрактного класса


class AnotherClass:  # 3) виртуальный класс

    def check(self, number):  # реализовали обязательный метод check
        if not isinstance(number, int):
            raise TypeError()
        for i in range(1, number):
            if i == 1:
                continue
            for j in range(2, number):
                if not number % j:
                    return False
                else:
                    return True

NumberValidatorPrime.register(AnotherClass)  # 3) регистрация класса как виртульного подкласса ABC класса

number_one = AnotherClass()
print(isinstance(number_one, NumberValidatorPrime))

number_two = SomeClass(1)
print(number_two.check(5))


# ---------------------------------------------2 ВАРИАНТ ОТ ОЛЕГА---------------------------------------------------


from abc import ABC, abstractmethod


class ABCMyIntNumber(ABC):

     @abstractmethod
     def isprime(self):
         pass


class MyIntNumber(ABCMyIntNumber):

    def __init__(self, number):
        self.number = number

    def isprime(self):
        if not isinstance(self.number, int):
            return False

        for i in range(2,self.number):
            if self.number % i == 0:
                return False
        return True

class MyIntNumber_1:

    def __init__(self, number):
        self.number = number


    def isprime(self):
        if not isinstance(self.number, int):
            return False

        for i in range(2,self.number):
            if self.number % i == 0:
                return False
        return True

x = MyIntNumber(7)
print(x.isprime())

y = MyIntNumber_1(10)
print(x.isprime())

print(isinstance(x, ABCMyIntNumber))
print(isinstance(y, ABCMyIntNumber))

ABCMyIntNumber.register(MyIntNumber_1)
print(isinstance(x, ABCMyIntNumber))
print(isinstance(y, ABCMyIntNumber))