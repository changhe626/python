def f(x):
    return x*x

r=map(f,[1,2,3,4])
#通过list()函数让它把整个序列都计算出来并返回一个list。
print(list(r))



L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)



#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
def add(x,y):
    return x+y

print(reduce(add,[1,2,3,4,4]))

