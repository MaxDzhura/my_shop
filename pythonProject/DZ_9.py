#home 1

s = set(input())
d = set(input())
res = s & d
print(res)

#home 2

a = [i for i in range(0,100,3)]
b = [i for i in range(0,100,5)]
print(set(a) & set(b))