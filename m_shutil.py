import shutil
"""
shutil
高级的 文件、文件夹、压缩包 处理模块
"""
# # 将文件内容拷贝到另一个文件中
# shutil.copyfileobj()  传入两个文件句柄， 一个源文件，另一个目标文件
shutil.copyfileobj(open('old.xml', 'r'), open('new.xml', 'w'))

# # 拷贝文件
# shutil.copyfile()  传入两个文件名
shutil.copyfile('f1.og', 'f2.log')  # 目标文件（f2.log）可以是一个不存在的文件

# # 仅拷贝权限。内容、组、用户均不变
# shutil.copymode
shutil.copymode('f1.log', 'f2.log')  # 目标文件必须存在

# # 拷贝文件状态的信息，包括：model bits,atime,mtime,flags
# shutil.copystat()
shutil.copystat('f1.log', 'f2.log')  # 目标文件必须存在

# # 拷贝文件和权限
# shutil.copy(src, dst)
shutil.copy('f1.log', 'f2.log')

# # 拷贝文件和状态信息
# shutil.copy2(src, dst)
shutil.copy2('f1.log', 'f2.log')

# # 递归的拷贝文件夹
# shutil.ignore_patterns(*patterns)
# shutil.copytree(src, dst, symlinks=False, ingore=None)
shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))
# 目标目录不能存在，注意对folder2目录腹肌目录要有可写权限，ignore的意思是排除

shutil.copytree('f1', 'f2', symlinks=True, ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))
# 通常的拷贝欸都把软连接拷贝成硬链接，即对带软连接老说创建新的文件 （symlinks）

# # 递归删除文件
# shutil.rmtree(path, ignore_errors=False, onerror=None)
shutil.rmtree('folder')


# # 递归移动文件，类似 mv 命令，其实就是重命名
# shutil.move
shutil.move('folder1', 'folder2')


# # 创建压缩包并返回文件路径，例如： zip、 tar
# shutil.make_archive(base_name, format, ...
# - base_name :　压缩包的文件名，也可以是压缩包的文件路径。只是文件名时，则保存到当前目录，否则保存到指定路径
# -- 如 data_bak   => 保存至当前路径
# -- 如 /tmp/data_bak => 保存至/tmp/
# - format:　压缩包种类　
# - root_dir: 要压缩的文件夹路径（默认当前目录）
# - owner： 用户，默认当前用户
# - group： 组，默认当前组
# - logger: 用于记录日志，通常是logging.Logger对象

# 将 /data 下的文件打包放到当前程序目录
ret= shutil.make_archive("data_bak", 'gztar', root_dir='/data')

# 将 /data 下的 文件打包放置 /tmp/ 目录
ret2 = shutil.make_archive("/tmp/data_bak", 'gztar', root_dir='/data')

# *注： 对压缩包的 处理是调用 zipfile 和 tarfile 两个模块来进行的，详细:

import zipfile
# 压缩
z = zipfile.ZipFile('laxi.zip', 'w')
z.write('a.log')
z.write('data.data')
z.close()

# 解压
z = zipfile.ZipFile('laxi.zip', 'r')
z.extractall(path='.')
z.close()

import tarfile
# 压缩
t = tarfile.open('/tmp/egon.tar', 'w')
t.add('/test1/a.py', arcname='a.bak')
t.add('/test1/b.py', arcname='b.bak')
t.close()

# 解压
t = tarfile.open('/tmp/egon.tar', 'r')
t.extractall('/egon')
t.close()
