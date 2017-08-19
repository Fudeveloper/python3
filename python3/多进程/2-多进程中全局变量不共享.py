import os
import time

g_num = 100
ret = os.fork()
if ret == 0:
    print('子进程')
    g_num += 1
    print('子进程结束  --- {0}'.format(g_num))

else:
    time.sleep(2)
    print('父进程')
    print('父进程  --- {0}'.format(g_num))

