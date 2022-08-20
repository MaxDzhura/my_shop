
# 1) Создайте декоратор, который будет подсчитывать, сколько раз была
# вызвана декорируемая функция.

def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper



@counter
def my_func(a):
    return a ** 2


my_func(22)
my_func(52)
my_func(10)
my_func(44)

print(my_func.count)


# ----------------------------------------2 ВАРИАНТ ОТ ОЛЕГА--------------------------------------------

def decorator(func):
    count = 0
    def inner(*args,**kwargs):
        nonlocal count
        count += 1
        return func(*args,**kwargs), count
    return inner


@decorator
def my_func(a):
    return a ** 2

print(my_func(5))
print(my_func(2))



# 2) Создайте декоратор, который зарегистрирует декорируемую функцию в
# списке функций, для обработки последовательности.


list_regist_func = []

def add_func(f):
    list_regist_func.append(f)
    return f

@add_func
def sum(x, y):
    return x + y

@add_func
def mul(x, y):
    return x * y

@add_func
def my_f(x, y):
    return x ** y

print(list_regist_func)


# ---------------------------------------------2 ВАРИАНТ ОТ ОЛЕГА---------------------------------------------------

func_list = []

def decorator(func):
    func_list.append(func)
    return func

@decorator
def x_2(item):
    return item ** 2

@decorator
def x_3(item):
    return item ** 3

seq = [i for i in range(10)]

for i in func_list:
    print(list(map(i,seq)))


# 3) Предположим, в классе определен метод __str__, который возвращает
# строку на основании класса. Создайте такой декоратор для этого метода,
# чтобы полученная строка сохранялась в текстовый файл, имя которого
# совпадает с именем класса, метод которого вы декорировали.


def decorator(func):
    def write_file(args):
        with open(args.__class__.__name__ + '.txt', 'a', encoding='utf-8') as file:
            file.write(func(args))
        return func(args)
    return write_file


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @decorator
    def __str__(self):
        return f'Название авто : {self.brand}, Модель: {self.model} \n'

car1 = Car('Toyota', "Corolla")
car2 = Car('Honda', "Accord")
print(car1, car2, sep='')

with open('Car.txt','r') as f:
    print(f.read())


# ---------------------------------------------2 ВАРИАНТ ОТ ОЛЕГА---------------------------------------------------

def decorator(func):
    def inner(*args, **kwargs):
        names = func.__qualname__.split('.')[:-1]
        file = '.'.join(names) + '.txt'
        res = func(*args, **kwargs)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(res)
        return res
    return inner


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @decorator
    def __str__(self):
        return f'Имя : {self.name}, Возраст: {self.age}'

p1 = Person('Vasya', 19)
p2 = Person('Jora', 22)
print(p1,p2, sep=' \n')


# 4) Создайте декоратор с параметрами для проведения хронометража работы
# той или иной функции. Параметрами должны выступать то, сколько раз нужно
# запустить декорируемую функцию и в какой файл сохранить результаты
# хронометража. Цель - провести хронометраж декорируемой функции.


import time


def func_parametr(zapuski, name_file):
    def func_decorator(f):
        def hronometr(*args, **kwargs):
            index = 0
            while index < zapuski:
                index += 1
                start = time.time()
                result = f(*args, **kwargs)
                end = time.time()
                with open(name_file + '.txt', 'w', encoding='utf-8') as file:
                    file.writelines(f"Количество запусков: {index}\nРезультат: {result}\nВремя работы : {end - start}\n")
            return f(*args, **kwargs)
        return hronometr
    return func_decorator



@func_parametr(3, 'func_mul')
def mul(a, b):
    return a * b


@func_parametr(3, 'func_plus')
def plus(a, b):
    return a + b


print(mul(4, 2))
print(plus(2, 5))

# ---------------------------------------------2 ВАРИАНТ ОТ ОЛЕГА---------------------------------------------------

import time

def decorator(file_name, number):
    def wrapper(func):
        def inner(*args, **kwargs):
            start = time.time()
            for i in range(number):
                res = func(*args, **kwargs)
            stop = time.time()

            with open(file_name + '.txt', 'a', encoding='utf-8') as f:
                f.write(f'{start}:{stop}: {stop-start}\n')
            return res
        return inner
    return wrapper

@decorator('Sobaken', 3)
def mul(a, b):
    return a * b

print(mul(153,654))



#------------ЗАДАНИЕ С 10 ЛЕКЦИИ:


# 1) Создайте декоратор, который зарегистрирует декорируемый класс в
# списке классов.

list_class = []

def add_class(cls):
    list_class.append(cls)
    return cls


@add_class
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Dog: {self.name}, Age: {self.age}"

@add_class
class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}"

dog1 = Dog('Chapa', 8)
cat1 = Cat('Barsik', 2.5)

print(dog1)
print(cat1)
print(list_class)
# МОЖНО  и так создат ьинстансы класса через список классов:

dog2 = list_class[0]('Bobik', 4)
cat2 = list_class[1]('Boss', 1)




# 2) Создайте декоратор класса с параметром. Параметром должна быть
# строка, которая должна дописываться (слева) к результату работы метода
# __str__.

def add_str(string):
    def decorator(cls):
        def wrapp(*args, **kwargs):
            return string + str(cls(*args, **kwargs))
        return wrapp
    return decorator



class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    @add_str('Класс с котами: ')
    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}"



cat1 = Cat('Bobik', 2)
print(cat1)


# ---------------------------------------------2 ВАРИАНТ ОТ ОЛЕГА---------------------------------------------------
# ДЕКОРАТОРОМ ВЫСТУПАЕТ ДРУГОЙ КЛАСС:

class Decoratorclass:
    def __init__(self,cls):
        self.param = 'Это наша коробка :'
        self.cls = cls

    def __call__(self,*args, **kwargs):
        self.new_instance = self.cls(*args, **kwargs)
        return self

    def __str__(self):
        return f'{self.param} {self.new_instance}'


@Decoratorclass
class Box:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"Box: a = {self.a}, b = {self.b}, c = {self.c}"

box_1 = Box(2, 3, 4)
box_2 = Box(5, 6, 7)
print(box_1)





# 3) Для класса Box напишите статический метод, который будет подсчитывать
# суммарный объем двух ящиков, которые будут его параметрами.


class Box:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"Box: a = {self.a}, b = {self.b}, c = {self.c}"

    def volume_box(self):
        return self.a * self.b * self.c

    @staticmethod
    def volume2_box(a1, b1, c1, a2, b2, c2):
        return a1 * b1 * c1 + a2 * b2 * c2


box_1 = Box(2, 3, 4)
box_2 = Box(5, 6, 7)
box_3 = Box.volume2_box(2, 3, 4, 5, 6, 7)
print(box_1.volume_box())
print(box_2.volume_box())
print(box_1, box_2, box_3, sep='\n')


# ---------------------------------------------2 ВАРИАНТ ОТ ОЛЕГА---------------------------------------------------

class Box:

    count = 0

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        Box.count += 1

    @classmethod               #КЛАС -МЕТОД РАБОТАЕТ С ПЕРЕМЕННЫМИ КЛАССА
    def boxes_number(cls):
        return cls.count

    def __str__(self):
        return f"Box: a = {self.a}, b = {self.b}, c = {self.c}"

    def volume_box(self):
        return self.a * self.b * self.c


    @staticmethod               #СТАТИК -МЕТОД РАБОТАЕТ БЕЗ ПРИВЯЗКИ К КЛАССАМ И ИНСТАНСАМ
    def summa_volume(a, b):
        if isinstance(a, Box) and isinstance(b, Box):
            return a.volume_box() + b.volume_box()
        return None


box_1 = Box(2, 2, 2)
box_2 = Box(3, 3, 3)
box_3 = Box(4, 4, 4)
box_4 = Box.summa_volume(box_1,box_2)
print(box_4)
print(box_1.volume_box())
print(Box.count)