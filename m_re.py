import re

# # \w 和 \W  相对的操作
print(re.findall('\w', 'hello world 123'))
# 输出： ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', '1', '2', '3']
print(re.findall('\W', 'hello world 123'))
# 输出： [' ', ' ']

# # \s 和 \S
print(re.findall('\s', 'hello world 123'))
# 输出： ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', '1', '2', '3']
print(re.findall('\S', 'hello world 123'))
# 输出： [' ', ' ']


# # '\n' '\t' 都是空 \s 匹配到
print(re.findall('\s', 'hello  \n world \t 123'))
# 输出： [' ', '\n', ' ', ' ', '\t', ' ']

# \n 与 \t
print(re.findall('\n', 'hello  \n world \t 123'))
# 输出： ['\n']
print(re.findall('\t', 'hello  \n world \t 123'))
# 输出： ['\t']

# \d 与 \D
print(re.findall('\d', 'hello world 123'))
# 输出： ['1', '2', '3']
print(re.findall('\D'))
# 输出： ['h', 'e', 'l', 'l', 'o', ' ', ' ', '\n', ' ', 'w', 'o', 'r', 'l', 'd', ' ', '\t', ' ']

# \A 与 \Z
print(re.findall('^h', 'hello world 123'))
# 输出： ['h']

print(re.findall('3$', 'hello world 123'))
# 输出： ['3']

# # 重复匹配 | . | * | ? | .* | .*? | + | {n,m} |

#  .
print(re.findall('a.b', 'a1b'))
# 输出： ['a1b']
print(re.findall('a.b', 'a1b a*b a b aaab'))
# 输出： ['a1b', 'a*b', 'a b', 'aab']
print(re.findall('a.b', 'a\nb'))  # . 在正常模式下不能匹配换行符
# 输出： []
print(re, findall('a.b', 'a\nb', re.S))  # 以整行形式匹配
# 输出： ['a\nb']
print(re.findall('a.b', 'a\nb', re.DOTALL))  # ['a\nb']同上一条意思一样
# 输出： ['a\nb']

# *
print(re.findall('ab*', 'bbbbbbb'))
# 输出： []
print(re.findall('ab*', 'a'))
# ['a']
print(re.findall('ab*', 'abbbb'))
# ['abbbb']

# ?
print(re.findall('ab?', 'a'))
# 输出： ['a']
print(re.findall('ab?', 'abbb'))
# 输出： ['ab']

print(re.findall('\d+\.?\d*', "asdfasdf123as1.13dfa12adsf1asdf3"))  # 匹配所有包含小数在内的数字
# 输出： ['123', '1.13', '12', '1', '3']


# .* 默认为贪婪匹配
print(re.findall('a.*b', 'a1b22222222222222b'))
# 输出： ['a1b22222222222222b']

# .*? 为非贪婪匹配： 推荐使用
print(re.findall('a.*?b', 'a1b22222222222222b'))
# 输出： ['a1b']

# +
print(re.findall('ab+', 'a'))
# 输出： []
print(re.findall('ab+', 'abbb'))
# 输出：['abbb']

# {n,m}个数
print(re.findall('ab{2}', 'abbb'))  # ['abb']
print(re.findall('ab{2,4}', 'abbb'))  # ['abb'] # 两个或四个
print(re.findall('ab{1,}', 'abbb'))  # 'ab{1,}' ===> 'ab+' # 1 到 任意
print(re.findall('ab{0,}', 'abbb'))  # 'ab{0,}' ===> 'ab*' # 0 到 任意

# [] 表示匹配集合  [^] 表示非匹配集合
print(re.findall('a[1*-]b', 'a1b a*b a-b'))  # 这里需要注意一下 '-' 作为字符匹配时建议放在最前边
# ['a1b', 'a*b', 'a-b']

print(re.findall('a[^1*-]b', 'a1b a*b a-b a=b'))  # []内的^代表的意思是取反，所以结果为['a=b']
# 输出： ['a=b']
print(re.findall('a[0-9]b', 'a1b a*b a-b a=b'))  # [0-9] 表示 0,1,2 ....7,8,9
# 输出： ['a1b']
print(re.findall('a[a-z]b', 'a1b a*b a-b a=b aeb'))  # 同理
# 输出： ['aeb']
print(re.findall('a[a-zA-Z]b', 'a1b a*b a-b a=b aeb aEb'))  # 同理
# 输出： ['aeb', 'aEb']

# \ # 最特殊的 转义字符匹配
print(re.findall('a\\c', 'a\c'))
# 对于正则来说a\\c确实可以匹配到a\c,但是在python解释器读取a\\c时，会发生转义，然后交给re去执行，所以抛出异常
print(re.findall(r'a\\c', 'a\c'))
# r代表告诉解释器使用rawstring，即原生字符串，把我们正则内的所有符号都当普通字符处理，不要转义
print(re.findall('a\\\\c', 'a\c'))
# 同上面的意思一样，和上面的结果一样都是['a\\c']

# () #分组
print(re.findall('ab+', 'ababab123'))  # ['ab', 'ab', 'ab']
print(re.findall('(ab)+123', 'ababab123'))  # ['ab']，匹配到末尾的ab123中的ab
print(re.findall('(?:ab)+123', 'ababab123'))  # findall的结果不是匹配的全部内容，而是组内的内容,?:可以让结果为匹配的全部内容
print(re.findall('href="(.*?)"', '<a href="http://www.baidu.com">点击</a>'))  # ['http://www.baidu.com']
print(re.findall('href="(?:.*?)"', '<a href="http://www.baidu.com">点击</a>'))  # ['href="http://www.baidu.com"']

# |
print(re.findall('compan(?:y|ies)', 'Too many companies have gone bankrupt, and the next one is my company'))

# =============== re模块提供方法介绍 ==============
import re

# 1 findall
print(re.findall('e', 'alex make love'))
# 输出： ['e', 'e', 'e'] ,返回所有满足匹配条件的结果,放在列表里

# 2 search->group
print(re.search('e', 'alex make love').group())
# 输出: e, 只到找到第一个匹配然后返回一个包含匹配信息的对象,
# 该对象可以通过调用 group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。

# 3 match
print(re.match('e', 'alex make love'))
# 输出: None
# 同 search,不过在字符串'开始'处进行匹配,完全可以用search+^代替match

# 4 split
print(re.split('[ab]', 'abcd'))
# ['', '', 'cd']，先按'a'分割得到''和'bcd',再对''和'bcd'分别按'b'分割

# 5 sub/subn
print('===>', re.sub('a', 'A', 'alex make love'))  # ===> Alex mAke love，不指定n，默认替换所有
print('===>', re.sub('a', 'A', 'alex make love', 1))  # ===> Alex make love  # 替换一个
print('===>', re.sub('a', 'A', 'alex make love', 2))  # ===> Alex mAke love  # 替换两个
print('===>', re.sub('^(\w+)(.*?\s)(\w+)(.*?\s)(\w+)(.*?)$', r'\5\2\3\4\1', 'alex make love'))
# ===> love make alex  # 分组匹配默认 按照 \1 \2 \3 \4 ... 序号

print('===>', re.subn('a', 'A', 'alex make love'))  # ===> ('Alex mAke love', 2),结果带有总共替换的个数

# 6 compile
obj = re.compile('\d{2}')
print(obj.search('abc123eeee').group())  # 12
print(obj.findall('abc123eeee'))  # ['12'], 重用了obj

# etc
import re

print(re.findall("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>", "<h1>hello</h1>"))  # ['h1']
print(re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>", "<h1>hello</h1>").group())  # <h1>hello</h1>
print(re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>", "<h1>hello</h1>").groupdict())  # <h1>hello</h1>

print(re.search(r"<(\w+)>\w+</(\w+)>", "<h1>hello</h1>").group())
print(re.search(r"<(\w+)>\w+</\1>", "<h1>hello</h1>").group())

# etc 2
import re

'''
print(re.findall(r"-?\d+\.\d*|(-?\d+)","1-2*(60+(-40.35/5)-(-4*3))")) #找出所有整数['1', '-2', '60', '', '5', '-4', '3']
#找到所有数字:
print(re.findall('\D?(\-?\d+\.?\d*)',"1-2*(60+(-40.35/5)-(-4*3))")) # ['1','2','60','-40.35','5','-4','3']

计算器作业参考：http://www.cnblogs.com/wupeiqi/articles/4949995.html
expression='1-2*((60+2*(-3-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

content=re.search('\(([\-\+\*\/]*\d+\.?\d*)+\)',expression).group() #(-3-40.0/5)
'''
print(re.findall(r"-?\d+\.\d*|(-?\d+)", "1-2*(60+(-40.35/5)-(-4*3))"))  # 找出所有整数['1', '-2', '60', '', '5', '-4', '3']

# 找到所有数字:
print(re.findall('\D?(\-?\d+\.?\d*)', "1-2*(60+(-40.35/5)-(-4*3))"))  # ['1','2','60','-40.35','5','-4','3']

# 计算器作业参考：http://www.cnblogs.com/wupeiqi/articles/4949995.html
expression = '1-2*((60+2*(-3-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

content = re.search('\(([\-\+\*\/]*\d+\.?\d*)+\)', expression).group()  # (-3-40.0/5)

# #为何同样的表达式search与findall却有不同结果:
print(re.search('\(([\+\-\*\/]*\d+\.?\d*)+\)', "1-12*(60+(-40.35/5)-(-4*3))").group())  # (-40.35/5)
print(re.findall('\(([\+\-\*\/]*\d+\.?\d*)+\)', "1-12*(60+(-40.35/5)-(-4*3))"))  # ['/5', '*3']

# 看这个例子:(\d)+相当于(\d)(\d)(\d)(\d)...,是一系列分组
print(re.search('(\d)+', '123').group())  # group的作用是将所有组拼接到一起显示出来
print(re.findall('(\d)+', '123'))  # findall结果是组内的结果,且是最后一个组的结果





