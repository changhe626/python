import time


print(time.time())
#1538030948.2398336

"""
序号	属性	值
0	tm_year	2008
1	tm_mon	1 到 12
2	tm_mday	1 到 31
3	tm_hour	0 到 23
4	tm_min	0 到 59
5	tm_sec	0 到 61 (60或61 是闰秒)
6	tm_wday	0到6 (0是周一)
7	tm_yday	一年中的第几天，1 到 366
8	tm_isdst	是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1
"""

print(time.localtime(time.time()))
#time.struct_time(tm_year=2018, tm_mon=9, tm_mday=27, tm_hour=14, tm_min=49, tm_sec=8, tm_wday=3, tm_yday=270, tm_isdst=0)

print(time.asctime(time.localtime(time.time())))
#Thu Sep 27 14:49:08 2018


print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
#2018-09-27 14:50:30


# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))