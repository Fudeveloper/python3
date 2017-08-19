import os
import time
ret = os.fork()

if ret==0:
    print('子进程 this={0},pid={1},ppid={2}'.format(ret,os.getpid(),os.getppid()))
else:
    print('父进程  this={0},pid={1},ppid={2}'.format(ret,os.getpid(),os.getppid()))

