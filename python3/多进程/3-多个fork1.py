import os
import time
ret = os.fork()
if ret == 0:
    # 子进程
    print('1')
else:
    # 父进程
    print('2')

res = os.fork()
if res == 0:
    print('11')
else:
    print('22')

time.sleep(5)
# 2
# 22
# 11
# 1
# 22
# 11