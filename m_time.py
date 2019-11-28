import time

print(time.time())  # 时间戳：1574400180.8635545
print(time.strftime("%Y-%m-%d %X"))  # 格式化字符串 '2019-11-22 13:24:01'
# 格式化字符串参考
'''
%a    Locale’s abbreviated weekday name.     
%A    Locale’s full weekday name.     
%b    Locale’s abbreviated month name.     
%B    Locale’s full month name.     
%c    Locale’s appropriate date and time representation.     
%d    Day of the month as a decimal number [01,31].     
%H    Hour (24-hour clock) as a decimal number [00,23].     
%I    Hour (12-hour clock) as a decimal number [01,12].     
%j    Day of the year as a decimal number [001,366].     
%m    Month as a decimal number [01,12].     
%M    Minute as a decimal number [00,59].     
%p    Locale’s equivalent of either AM or PM.    (1)
%S    Second as a decimal number [00,61].    (2)
%U    Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.    (3)
%w    Weekday as a decimal number [0(Sunday),6].     
%W    Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.    (3)
%x    Locale’s appropriate date representation.     
%X    Locale’s appropriate time representation.     
%y    Year without century as a decimal number [00,99].     
%Y    Year with century as a decimal number.     
%z    Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM, where H represents decimal hour digits and M represents decimal minute digits [-23:59, +23:59].     
%Z    Time zone name (no characters if no time zone exists).     
%%    A literal '%' character.
'''
# 图 https://images2015.cnblogs.com/blog/1036857/201702/1036857-20170215142700722-743334012.png

print(time.localtime())  # 本地时区 struct_time : time.struct_time(tm_year=2019, ... ,tm_isdst=0) tm_hour=13,
print(time.gmtime())  # utc 时区时间 struct_time: time.struct_time(tm_year=2019, ... ,tm_isdst=0) tm_hour=5,

# 三种是时间转换
# 格式化字符串时间(format string)  <=>  结构化时间(struct_time)  <=> 时间戳(timestamp)


# # 时间戳转换成为当前时区 struct_time。
# localtime([secs])当 secs 参数未提供，则以当前时间为准
print('时间戳转换成为当前时区struct_time'.center(50, '-'))
print('默认（当不传secs）显示当前:', time.localtime())
print('传入参数secs:', time.localtime())
print('used: time.localtime()')
# gmtime([secs]) 和 localtime() 方法类似 gmtime() 方法是将一个时间转换为 UTC(0时区) struct_time.

# # 将一个struct_time 转化为时间戳
# mktime(t)
print('struct_time 转化为时间戳'.center(50, '-'))
print(time.mktime(time.localtime()))  # time.localtime() 返回是 'struct_time'  转换为 '时间戳'
print('used: time.mktime()')

# # 把一个代表时间的元祖或者struct_time(如由time.localtime()和time.gmtime()返回) 转化为格式化时间字符串。
# 如果 t 为指定，将传入 time.localtime(). 如果元组中任何一个元素越界，ValueError 的错误将被抛出
# time.strftime()
print('struct_time 或者代表时间元组转为format string time'.center(50, '-'))
print(time.strftime('%Y-%m-%d %X', time.localtime()))
print('used: time.strftime()')

# # 把一个格式化字符串时间转化为 struct_time。 实际上它和strftime()是逆操作。
# time.strptime('2011-06-25 15:54:12', '%Y-%m-%d %X') '%Y-%m-%d %X' 时间格式
print('格式化字符串时间转化为 struct_time'.center(50, '-'))
print(time.strptime('2011-06-25 15:54:12', '%Y-%m-%d %X'))  # 函数默认为 "%a %b %d %H:%M:%S %Y"
print('used: time.strptime(字符串时间, 格式化)')

# 图 https://images2015.cnblogs.com/blog/1036857/201702/1036857-20170215143428754-2105818567.png
# # asctime([t]): 把一个时间的元组或者struct_time 表示为： 'Sun Jun 20 23:21:05 1993'
# 如果没有穿参数，默认是将　time.localtime() 作为参数传入
# time.asctime()
print('将时间的元组或者struct_time转为 英文 周 月'.center(50, '-'))
print(time.asctime())
print('used: time.asctime()')

# # ctime([secs]) : 把一个时间戳(按秒计算的浮点数) 转化为  time.asctime() 的形式。如果没传参数或者为 None 的时候，
# 将会默认 time.time() 作为参数。它的作用相当于 time。asctime(time.localtime(secs)).
# time.ctime()
print('把时间戳转换为 英文格式 周 月'.center(50, '-'))
print(time.ctime())
print(time.ctime(time.time()))  # 1574403032.5256188  => 'Sun Jun ...'
print('used: time.ctime()')

#  # etc  time.sleep()
# 线程推迟 指定时间运行，单位为秒。
print('time.sleep()'.center(50, '-'))
print('execute time.sleep(3)')
# time.sleep(3)  # 推迟3秒
print('used: time.sleep()')

# ## datetime
# 做时间加减
import datetime

# # datime.datetime.now() 返回字符串格式时间
print('datetime.now()'.center(50, '-'))
print(datetime.datetime.now())
print('used: datetime.now()')

# # 时间戳直接转化为 字符串格式时间
# datetime.date.fromtimestamp(time.time())  # time.time() 是时间戳
print('时间戳直接转化为 字符串格式时间'.center(50, '-'))
print(datetime.date.fromtimestamp(time.time()))  # date / datetime
print('used: datetime.date.fromtimestamp')

# # datetime.timedelta() 时间加减
print("时间加减：")
print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(3))  # 当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3))  # 当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3))  # 当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30))  # 当前时间+30分
print('used: datetime.timedelta(...)')

# # 时间替换
# replace()
print('时间替换'.center(50, '-'))
c_time = datetime.datetime.now()
print(c_time, 'is replaced to', c_time.replace(minute=2, hour=2))
