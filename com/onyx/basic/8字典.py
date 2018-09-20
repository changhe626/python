"""
字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
"""

dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(dict)


print(dict["Alice"])
# print(dict["Alice2"])   不存在的key会报错



dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8;  # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

del dict['Name'] # 删除键 'Name'
dict.clear()     # 清空字典
del dict         # 删除字典,删除之后再引用就会报错了...


# 字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行


"""
1	len(dict)
计算字典元素个数，即键的总数。	

3
2	str(dict)
输出字典，以可打印的字符串表示。	

3	type(variable)
返回输入的变量类型，如果变量是字典就返回字典类型。
"""


"""
Python字典包含了以下内置方法：


1	
radiansdict.clear()
删除字典内所有元素

2	
radiansdict.copy()
返回一个字典的浅复制

3	
radiansdict.fromkeys()
创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值

4	
radiansdict.get(key, default=None)
返回指定键的值，如果值不在字典中返回default值

5	
key in dict
如果键在字典dict里返回true，否则返回false

6	
radiansdict.items()
以列表返回可遍历的(键, 值) 元组数组

7	
radiansdict.keys()
返回一个迭代器，可以使用 list() 来转换为列表


8	
radiansdict.setdefault(key, default=None)
和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default

9	
radiansdict.update(dict2)
把字典dict2的键/值对更新到dict里

10	
radiansdict.values()
返回一个迭代器，可以使用 list() 来转换为列表

11	
pop(key[,default])
删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。

12	
popitem()
随机返回并删除字典中的一对键和值(一般删除末尾对)。
"""