import random

# 生成随机数字的模块
print(random.random())  # (0, 1) -- float (0, 1)生成 (0 到 1) 之间小数（浮点数）

print(random.randint(1, 3))  # [1,3]    大于等于1且小于等于3之间的整数  random.randint = random.randrange(0,10,1)

print(random.randrange(1, 3))  # [1,3)    大于等于1且小于3之间的整数

print(random.choice([1, '23', [4, 5]]))  # 1或者23或者[4,5]

print(random.sample([1, '23', [4, 5]], 2))  # 列表元素任意2个组合

print(random.uniform(1, 3))  # 大于1小于3的小数，如1.927109612082716

items = [1, 3, 5, 6, 9]
random.shuffle(items)  # 打乱 itmes 的顺序， 相当于 ”洗牌“
print(items)


# eg: 生成随机验证码
def make_code(n):
    res = ''
    for i in range(n):
        s1 = chr(random.randint(65, 90))
        s2 = str(random.randint(0, 9))
        res += random.choice([s1, s2])
    return res


print(make_code(9))

'''
randint(start, end) 相当于 randrange(start, end, 1)

也就是说：
randint 产生的数据start 和 end 之间的任意数，
randrange 可以产生跳跃的数据，比如要产生一个 100 - 200 之间的偶数，就可以用 randrange(100, 200, 2)
'''
print(__file__)