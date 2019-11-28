import os

os.getcwd()  获取当前工作目录路径
os.getcwdb()   获取当前工作目录路径bytes ==>  b''
os.chdir("")  改变当前脚本工作目录；相当于shell 下边的 cd
os.curdir  返回当前目录 '.'
os.pardir  返回当前目录的父目录的字符串名 '..'
os.makedirs('dirname1/dirname2')  可生成多层递归目录
os.removedirs('dirname1') 如果目录为空，则删除，并且递归到上一级目录，如果也为空，则删除，以此类推  递归删除空目录
os.mkdir('dirname')  生成单级目录。相当于 shell 中 mkdir dirname
os.rmdir('dirname')  删除单级空目录，若目录不为空则无法删除，报错，相当于 shell 中的 rmdir dirname
os.listdir('dirname')  列出制定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove('filename')  删除一个存在的文件，不存在则报错
os.rename('oldname', 'newname') 重命名文件/目录 文件/目录不存在则报错
os.stat('filename/path')  获取文件/目录的信息
os.sep  返回操作系统特定路径分隔符 win '\\', linux 为 "/"
os.linesep  返回当前平台使用的终止符号 win下为"\t\n" linux 下为"\n"
os.pathsep  返回分隔路径的字符 win下为 ';' linux 下为 ':'
os.name   f安徽操作系统使用平台 win -> 'nt'; Linux -> 'posix'
os.system("bash command")  运行shell 命令，直接显示
os.environ  获取系统环境变量

---- os.path ---
os.path.abspath('filename/path')  返回 path 规范会绝对路径 文件/目录
os.path.split('path')  将path 分割成目录和文件名二元组返回

os.path.dirname('path')  返回 path 的目录，其实就是 os.path.split(path) 的第一个元素
os.path.basename('path')  返回 path 最后的文件名，如果 path以 '/' 或 `\` 结尾，那么返回空, 即 os.path.split(path) 的第二个元素
os.path.exists('path')  判断path(文件/目录)是否存在 存在返回 True
os.path.isabs('path')  判断path 是否是绝对路径 是返回 True
os.path.isfile('path')  判断 path(文件/目录) 是不是文件 是返回 True
os.path.isdir('path')  判断 path(文件/目录) 是不是一个目录 是返回True
os.path.join(path1[path2, ...]) 将多个路径组合后返回，注意第一个绝对路径之前的参数将被忽略
os.path.getatime('path')  返回 path(文件/目录) 所子项的文件或者目录的最后存取时间
os.path.getmtime('path')  返回 path(文件/目录) 所子项的文件或者目录的最后修改时间
os.path.getsize('path to filename| filename')  返回 path 的大小, 如果传入的是目录 则返回 0

# # 对比：
'''
在Linux和Mac平台上，该函数会原样返回path，在windows平台上会将路径中所有字符转换为小写，并将所有斜杠转换为饭斜杠。
>> > os.path.normcase('c:/windows\\system32\\')
'c:\\windows\\system32\\'

规范化路径，如..和 /
>> > os.path.normpath('c://windows\\System32\\../Temp/')
'c:\\windows\\Temp'

>> > a = '/Users/jieli/test1/\\\a1/\\\\aa.py/../..'
>> > print(os.path.normpath(a))
/ Users / *** / test1
'''

'''
os路径处理
#方式一：推荐使用
import os
#具体应用
import os,sys
possible_topdir = os.path.normpath(os.path.join(
    os.path.abspath(__file__),
    os.pardir, #上一级
    os.pardir,
    os.pardir
))
sys.path.insert(0,possible_topdir)


#方式二：不推荐使用
os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
'''