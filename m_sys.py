sys.argv        命令行参数 List，第一个元素是程序本身路径（python脚本路径）
sys.exet(n)     退出程序，正常退出 exit(0)
sys.version     获取Python 解释程序的版本信息
sys.maxint      最大的 Int 值
sys.plantform   系统操作平台名称

# ------ 只是储备 ------
# 进度条效果
[#             ]
[##            ]
[###           ]
[####          ]

#指定宽度
print('[%-15s]' %'#')
print('[%-15s]' %'##')
print('[%-15s]' %'###')
print('[%-15s]' %'####')

# 打印出 '%'
print('%s%%' % (100))  # 第二个 % 号代表取消第一个 % 的特殊意义

# 可传参控制宽度
print('[%%-%ds]' %50)  #[%-50s]
print(('[%%-%ds]' %50) %'#')
print(('[%%-%ds]' %50) %'##')
print(('[%%-%ds]' %50) %'###')

应用：
# ======= 实现进度条函数 ======
import sys
import time

def progress(percent, width=50):
    if percent >= 1:
        percent=1
    show_str = ('[%% -%ds]' %width) % (int(width*percent)*'#')
    print('\r%s %d%%')% (show_str, int(100*percent)), file=sys.stdout, flush=True, end='')


# ====== 应用 ======
data_size=1025
recv_size=0
while recv_size < data_size:
    time.sleep(.1)  # 模拟数据传输延迟
    recv_size += 1024 # 每次接受 1024

    percent = recv_size / data_size  # 接收的比例
    progress(percent, width=70)  # 进度条的宽度70
