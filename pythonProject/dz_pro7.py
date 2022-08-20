# 1) Реализуйте генераторную функцию, которая будет возвращать по
# одному члену геометрической прогрессии с указанным множителем.
# Генератор должен остановить свою работу или по достижению указанной
# границы, или при передаче команды на завершение.


def geometric_progress(n, stop):
    res = 1
    while res <= stop:
        yield res
        res *= n
    return

for i in geometric_progress(2, 500):
    print(i, end=' ')


# 2) Реализуйте свой аналог генераторной функции range(). Да, вы теперь
# знаете, что это - генератор.


def range_analog(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    while start < stop:
        yield start
        start += step

for i in range_analog(10):
    print(i, end=' ')



# 3) Напишите функцию-генератор, которая будет возвращать простые числа.
# Верхняя граница этого диапазона должна быть задана параметром этой
# функции.


def prime_num(stop):
    for i in range(1, stop-1):
        if i == 1:
            continue
        for j in range(2, i):
            if not i % j:
                break
        else:
            yield i
    return

for i in prime_num(100):
    print(i)


# 4) Напишите выражение-генератор для заполнения списка. Список должен
# быть заполнен кубами чисел от 2 и до указанной вами величины.

n = int(input("Введите цифру:"))
mylist = (i ** 3 for i in range(2, n))
for i in mylist:
    print(i)