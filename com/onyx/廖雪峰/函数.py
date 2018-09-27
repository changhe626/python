#返回多个参数
def print2(a,b,c):
    print(a,b,c)
    return a+1,b+1



x,y=print2(1,2,3)
print(x,y)