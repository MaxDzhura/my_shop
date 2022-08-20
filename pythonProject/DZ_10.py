# home 1
a,b,c = int(input("a:")),int(input("b:")),int(input("c:"))

def maxx (a,b,c):
    if a > b:
        if a > c:
            print(a)
        else:
            print(c)
    elif b > c:
        print(b)
    else:
        print(c)
maxx(a,b,c)

# home 1 второй вариант

a = [20,65,6556,5,989,49,954]

def max2 (a):
    print(max(a))
max2(a)


# home 2

a,b,c = 155,10,"mmm"
def plus(a,b,c):
    res = a + b
    return str(res) + c
print(plus(a,b,c))


# home 3

m,n = int(input("m:")),int(input("n:"))
def figur(a,b):
    for i in range(b):
        for j in range(a):
            print("* ", end="")
        print(" ")
figur(m,n)


# home 4


sp = [10,20,30,40,45,50,80,95]
vvod = int(input("vvod :"))
def search(sp,vvod):
    for i in range(len(sp)):
        if sp[i] == vvod:
            return i
    return "нет в списке"
print(search(sp,vvod))


# home 5

a = input("vvod :")
def func(b):
    while "  " in b:
        b = b.replace("  ", " ")
    return b.count(" ") + 1
print(f" Количество слов в тексте : {func(a)}")


# home 6

ff = input().split(",")
def posl(a):
    res = str(a)
    return int(a[-1]) + 5
print(posl(ff))


# home 7 ( Вывел только палиндром, произведение чисел вывести не получилось)


def polin(num):
    raw = str(num)
    rnum = int(raw[::-1])
    if num  == rnum:
        return True
    else:
        return False
sp = []
for i in range(100,1000):
    for j in range(100,1000):
        if polin(i*j) == True:
            sp.append(i*j)
print(max(sp))
