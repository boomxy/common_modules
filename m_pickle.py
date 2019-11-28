'''
序列化介绍参考 m_json.py 中
图： https://images2015.cnblogs.com/blog/1036857/201702/1036857-20170215164644722-1590025858.png
'''

import pickle

dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}

print(type(dic))  # <class 'dict'>

j = pickle.dumps(dic)
print(type(j))  # <class 'bytes'>

f = open('序列化对象_pickle', 'wb')  # 注意是w是写入str,wb是写入bytes,j是'bytes'
f.write(j)  # -------------------等价于pickle.dump(dic,f)

f.close()
# -------------------------反序列化

f = open('序列化对象_pickle', 'rb')

data = pickle.loads(f.read())  # 等价于data=pickle.load(f)

print(data['age'])
