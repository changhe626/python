a=1
print(a)
b=1.4
c="f"
a=4.6
print(a)
a="sa"
print(a)
print(b)


a = b = c = 1

a, b, c = 1, 2, "runoob"

"""
Python3 中有六个标准的数据类型：
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）
"""

#Number（数字）
#Python3 支持 int、float、bool、complex（复数）。
#内置的 type() 函数可以用来查询变量所指的对象类型。
print(type(a),type(b),type(c))
#type()不会认为子类是一种父类类型。
#isinstance()会认为子类是一种父类类型。
print(isinstance(a,int))
print(isinstance(a,str))

print("~~~~")

class A:
    pass

class B(A):
    pass

print(isinstance(A(), A))  # returns True
print(type(A()) == A)      # returns True
print(isinstance(B(), A))    # returns True
print(type(B()) == A)        # returns False



"""
1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
4、在混合计算时，Python会把整型转换成为浮点数。

"""
a, b = 1, 2

print(a/b)
print(a//b)


"""
Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。

字符串的截取的语法格式如下：

变量[头下标:尾下标]

Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：

注意：

1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变。
"""


word="python"
print(word[0:1],word[1:2])

print('Ru\noob')
print(r'Ru\noob')


"""
List（列表）
索引值以 0 为开始值，-1 为从末尾的开始位置。
加号 + 是列表连接运算符，星号 * 是重复操作

注意：

1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的。
"""
list=[1,1,3,4,6,'a']
tinylist=["x","y"]

print(list[0])
print(list[-1])
print(list[0:3])
print(list[0:6])

print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表


"""
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

元组中的元素类型也可以不相同

string、list和tuple都属于sequence（序列）。

注意：
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含0或1个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接。
"""
tup =("a","a",3,6)
print(tup[0])
print(tup[1:5])
#tup[0] = 11  # 修改元组元素的操作是非法的


tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号


"""
Set（集合）
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。

基本功能是进行成员关系测试和删除重复元素。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""

print("~~~~")
a=set()
print(a)
a=set("a")   #这种方式,只能创建一个元素的...
print(a)

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)  # a和b的差集

print(a | b)  # a和b的并集

print(a & b)  # a和b的交集

print(a ^ b)  # a和b中不同时存在的元素


"""
Dictionary（字典）
字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。


注意：
1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。
"""


dict={}
print(dict)
dict["a"]="A"
dict["b"]="b"
dict["b"]="b2"  #覆盖了
print(dict)


tinydict ={"a":"A","2":2}

print (dict['a'])       # 输出键为 'one' 的值
print (dict["b"])           # 输出键为 2 的值,没有这个key就直接报错了
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

#构造函数 dict() 可以直接从键值对序列中构建字典如下：
#dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])   #这个是在命令行中...这里会报错

{x: x**2 for x in (2, 4, 6)}

dict(Runoob=1, Google=2, Taobao=3)


"""
int(x [,base])
将x转换为一个整数

float(x)
将x转换到一个浮点数

complex(real [,imag])
创建一个复数

str(x)
将对象 x 转换为字符串


repr(x)
将对象 x 转换为表达式字符串

eval(str)
用来计算在字符串中的有效Python表达式,并返回一个对象

tuple(s)
将序列 s 转换为一个元组

list(s)
将序列 s 转换为一个列表

set(s)
转换为可变集合

dict(d)
创建一个字典。d 必须是一个序列 (key,value)元组。

frozenset(s)
转换为不可变集合

chr(x)
将一个整数转换为一个字符

ord(x)
将一个字符转换为它的整数值

hex(x)
将一个整数转换为一个十六进制字符串

oct(x)
将一个整数转换为一个八进制字符串
"""


