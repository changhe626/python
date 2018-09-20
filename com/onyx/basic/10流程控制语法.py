"""
Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。

注意：

1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3、在Python中没有switch – case语句。

"""

var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)
else:
    print("Good bye!")




#同样需要注意冒号和缩进。另外，在Python中没有do..while循环。

sum = 0
counter = 1
while counter <= 100:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (100, sum))



"""
while 循环使用 else 语句
在 while … else 在条件语句为 false 时执行 else 的语句块：
"""
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")



"""
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

for循环的一般格式如下：

for <variable> in <sequence>:
    <statements>
else:
    <statements>
"""

languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)


sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")



"""
如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:
"""

for x in range(6):
    print(x,end=",")
print("~~~")
for x in range(2,6):
    print(x,end=",")
print("~~~")
for x in range(1, 6,2):
    print(x, end=",")



a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

"""
break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。 

continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
"""



"""
循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。

如下实例用于查询质数的循环例子:
"""
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')


"""
Python pass是空语句，是为了保持程序结构的完整性。

pass 不做任何事情，一般用做占位语句，如下实例
"""

for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")