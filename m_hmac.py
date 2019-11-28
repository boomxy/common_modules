import hmac
h = hmac.new('alvin'.encode('utf-8'))
h.update('hello'.encode('utf-8'))
print(h.hexdigest())  # 320df9832eab4c038b6c1d7ed73a5940


# 要保证hamc最终结果一直，必须保证；
# 1. hmac.new 括号内执行的初始化key一样
# 2. 无论update多少次，校验的内容累加到一起是一样的内容

h1 = hmac.new(b'egon')
h1.update(b'hello')
h1.update(b'world')
print(h1.hexdigest())  

h2=hmac.new(b'egon')
h2.update(b'helloworld')
print(h2.hexdigest())

#  h1 = h2 != h3

h3=hmac.new(b'egonhelloworld')
print(h3.hexdigest())