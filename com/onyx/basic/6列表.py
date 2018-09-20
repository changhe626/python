"""
序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推


"""

list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 1, 3, 4, 5, 6, 7];

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

list1[1]="microsoft"
print(list1)

#删除列表元素
del list1[3]
print(list1)

#del list1[3]  #删除不存在的时候报错

"""
len([1, 2, 3])	    3	长度
[1, 2, 3] + [4, 5, 6]	         [1, 2, 3, 4, 5, 6]	  组合
['Hi!'] * 4	       ['Hi!', 'Hi!', 'Hi!', 'Hi!']	    重复
3 in [1, 2, 3]	             True	元素是否存在于列表中
for x in [1, 2, 3]: print(x, end=" ")	          1 2 3	迭代

"""

print( "a" in list1)

for x in list1:print(x,end="#")


"""
1	
len(list)
列表元素个数

2	
max(list)
返回列表元素最大值

3	
min(list)
返回列表元素最小值

4	
list(seq)
将元组转换为列表
"""


"""
1	
list.append(obj)
在列表末尾添加新的对象

2	
list.count(obj)
统计某个元素在列表中出现的次数

3	
list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）


4	
list.index(obj)
从列表中找出某个值第一个匹配项的索引位置

5	
list.insert(index, obj)
将对象插入列表

6	
list.pop([index=-1]])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

7	
list.remove(obj)
移除列表中某个值的第一个匹配项

8	
list.reverse()
反向列表中元素

9	
list.sort(cmp=None, key=None, reverse=False)
对原列表进行排序

10	
list.clear()
清空列表

11	
list.copy()
复制列表

"""