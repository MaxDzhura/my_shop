# 1/ Реализуйте генераторную функцию, которая будет возвращать по одному
# члену числовой последовательности, закон которой задается с помощью
# пользовательской функции. Кроме этого параметром генераторной функции
# должны быть значение первого члена прогрессии и количество выдаваемых
# членов последовательности (n). Генератор должен остановить свою работу
# или по достижению n — го члена, или при передаче команды на завершение.


# 1 variant
def generator_func(start, stop, rulefunc):
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError
    for i in rulefunc(start, stop):
        yield i


def rule_mul(a, end):
    res = []
    while len(res) < end:
        res.append(a * 2)
        a += 1
    return res


def rule_sqrt(a, end):
    res = []
    while len(res) < end:
        res.append(a ** 2)
        a += 1
    return res


res = generator_func(1, 20, rule_sqrt)
for i in res:
    print(i, end=' ')


# 2 -------------------------------------variant----------------------------------
# ТУт ни какие данные не хранятся в списке( по сути настоящий генератор)


def get_next_item(start, step, n, func):

    items = (func(start, step, i )for i in range(n))
    while True:
        try:
            yield next(items)
        except:
            break


def arithmetic_progression(a_0, dx, n):
    return a_0 + n * dx

def geometric_progression(b_0, q, n):
    return b_0 * q ** (n - 1)



print(*get_next_item(10, 2, 20, arithmetic_progression))
print(*get_next_item(1, 2, 20, geometric_progression))



# 2/ Используя функцию замыкания реализуйте такой прием программирования
# как Мемоизация - https://en.wikipedia.org/wiki/Memoization
# Используйте полученный механизм для ускорения функции рекурсивного
# вычисления n — го члена ряда Фибоначчи. Сравните скорость выполнения с
# просто рекурсивным подходом.


import functools
import timeit

# ---------функция Фибоначчи ЧЕРЕЗ ЗАМЫКАНИЕ------


def fibonacci():
     spisok = [0,1]

     def get_spisok(n):
         if n < len(spisok):
             return spisok[n]

         curr_item, next_item = spisok[-2], spisok[-1]
         i = len(spisok)

         while i <= n:
             curr_item, next_item = next_item, curr_item + next_item
             spisok.append(next_item)
             i = i + 1
         return next_item

     return get_spisok


x = fibonacci()
for i in range(10):
    print(x(i), end=" ")

print()
print(x(7))


# ---------Рекурсивная функция Фибоначчи:------

@functools.lru_cache
def fibonacci_recursion(n):
    if n in {0,1}:
        return n
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

print(fibonacci_recursion(10))


print(timeit.timeit("fibonacci_recursion(20)", number=5, setup="from __main__ import fibonacci_recursion" ))
print(timeit.timeit("x(20)", number=5, setup="from __main__ import x" ))






# 3/ Напишите функцию, которая применит к списку чисел произвольную
# пользовательскую функцию и вернет суммы элементов полученного списка


listnum = [20, 15, 44, 90, 33, 70]
res = sum(list(map(lambda x: x * 3, listnum)))
print(res)


# 2 -------------------------------------variant---------------------------------- Этой задачи

def my_func(seq, func_tool):
    return sum(func_tool(i) for i in seq)


def x_2(item):
    return item ** 2

def x_3(item):
    return item ** 3

def x_increment(item):
    return item + 1

def x_decrement(item):
    return item - 1

list_1 = [20, 15, 8, 4, 33, 70, 10]

print(my_func(list_1, x_2))
print(my_func(list_1, x_increment))
print(my_func(list_1, x_3))
print(my_func(list_1, x_decrement))

print(my_func(list_1, lambda x: x // 2))