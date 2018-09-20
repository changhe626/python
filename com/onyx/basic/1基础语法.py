# 单行注释
''' 多行注释 '''
""" 多行注释 """

#关键字
import keyword
print(keyword.kwlist)

#if ,else
if True:
    print("true")
else:
    print("false")

#Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：
string="a" \
           "b" \
           "c" \
           "d;"

print(string)

"""
python中数字有四种类型：整数、布尔型、浮点数和复数。
int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j
"""


#字符串的截取的语法格式如下：变量[头下标:尾下标]
str="wangzhaojun"
print(str)
print(str[0:100])  #全部
# print(str[0,0])  错误
print(str[0:1])

print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + ':你好')        # 连接字符串


print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
#这里的 r 指 raw，即 raw string。



#等待用户输入
# input("\n\n 按下enter建后退出")
#以上代码中 ，"\n\n"在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。



#Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：

import sys;x="runoob";sys.stdout.write(x+"\n")


#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：

print("hell",end="")
print("hell2",end="")


"""
将整个模块(somemodule)导入，格式为： import somemodule

从某个模块中导入某个函数,格式为： from somemodule import somefunction

从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为： from somemodule import *

"""



