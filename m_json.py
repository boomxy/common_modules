'''
# # 什么事序列化？
    我们把对象(变量)从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，\
在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

# # 为什么要序列化？
1 : 持久保存状态

2 : 跨平台数据交互
    序列化之后，不仅可以把序列化后的内容写入磁盘，还可以通过网络传输到别的机器上，如果收发的双方约定好实用一种序列化的格式，
那么便打破了平台/语言差异化带来的限制，实现了跨平台数据交互。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。


# # 如何序列化之 json 和 pickle
如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，
但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

图： https://images2015.cnblogs.com/blog/877318/201609/877318-20160911105642628-530508765.png
图2：https://images2015.cnblogs.com/blog/1036857/201702/1036857-20170215162939035-339680318.png
'''

import json

dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}
print(type(dic))  # <class 'dict'>

j = json.dumps(dic)
print(type(j))  # <class 'str'>

f = open('序列化对象', 'w')
f.write(j)  # -------------------等价于json.dump(dic,f)
f.close()

import json

f = open('序列化对象')
data = json.loads(f.read())  # 等价于data=json.load(f)
# 此时 data 的值就是最开始的 dic 的值

# * 注意 json 不认单引号
# dct="{'1':111}"#json 不认单引号
# dct=str({"1":111})#报错,因为生成的数据还是单引号:{'one': 1}

dct = '{"1": "111"}'
print(json.loads(dct))

# ex：无论数据是怎样创建的，只要满足json格式i，就可以json.loads 出来
