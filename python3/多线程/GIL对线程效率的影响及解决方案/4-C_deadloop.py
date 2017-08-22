from threading import Thread
import ctypes

# 加载库
deadloop_lib = ctypes.cdll.LoadLibrary('./libdeadloop.so')

DeadLoop = deadloop_lib.DeadLoop
t = Thread(target=DeadLoop)
t.start()

DeadLoop()