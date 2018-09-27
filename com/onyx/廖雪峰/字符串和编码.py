"""
对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：

"""

print(ord("A"))
print(chr(66))

"""
以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
"""

print( 'ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
#print('中文'.encode('ascii'))

"""
如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：

"""
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))





