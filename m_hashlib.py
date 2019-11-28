'''
1. 什么叫hash？
	hash 是一种算法 （3.x 里边代替了 md5 模块和 sha 模块，
	主要提供 SHA1、SHA256、SHA384、SHA512、MD5算法），经过运算得到的一串 hash 值
2. hash值的特点
	1. 只要传入的内容一样，得到的hash 值必然是一样的 ===> 要用明文传输密码完整性验
	2. 不能由 hash 值反解成内容 ===> 把密码做成hash 值，不应该在网络上传输明文密码
	3. 只要使用的hash 算法不变，无论校验的内容有多大，得到的hash 值长度是固定的
'''

import hashlib

m = hashlib.md5()  # m = hashlib.sha256()
m = m.update('hello'.encode('utf-8'))  # encode 是因为 haslib 只加密 bytes 串 否则会报错
print(m.hexdigest())  # 5d41402abc4b2a76b9719d911017c592

m.update('alvin'.encode('utf-8')
print(m.hexdigest())  # 92a7e713c30abbb0319fa07da2a5c4af

m2 = hashlib.md5()
m2.update('helloalvin'.encode('utf-8')
print(m2.hexdigest())  # 92a7e713c30abbb0319fa07da2a5c4af

# * 注 这里把很长的数据update 多次，与以此update这段长数据，得到的结果一样，单数 update多次为校验大文件提供了可能。


# 以上加密算法虽然依然非常厉害，但时候存在缺陷，即：通过撞库可以反解。所以，有必要对加密算法中添加自定义key再来做加密。

# # ========== sha256 ==========
import hashlib

hash = hashlib.sha256('89oafsf'.encode('utf-8'))
hash.update('alvin'.encode('utf-8'))
print(hash.hexdigest()) # 37a16b3d841a3615a2044e4d53ff10a318f9f9a6b7c759f62337b21033d3c269


# # 模拟撞库破解密码
import hashlib
passwds=[
    'alex3714',
    'alex1313',
    'alex94139413',
    'alex123456',
    '123456alex',
    'a123lex',
    ]
def make_passwd(passwds):
dic={}
    for passwd in passwds:
        m = hashlib.md5()
        m.update(passwd.encode('utf-8'))
        dic.[passwd] = m.hexdigest()
    return dic
    
def break_code(cryptograph, passwd_dic):
    for k, v in passwd_dic.items():
        if v == cryptograph:
            print("密码是 ---> %s" %k)

cryptograph='aee949757a2e698417463d47acac93df'
break_code(cryptograph,make_passwd_dic(passwds))

# python 还有一个hmac 模块，他内部对我们创建 key 和 内容进行进一步处理，然后加密：
# 详见 m_hmac.py

