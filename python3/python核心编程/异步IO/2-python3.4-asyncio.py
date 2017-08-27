import asyncio

@asyncio.coroutine
def hello():
    print('hello world')
    # 用asyncio.sleep来模拟IO阻塞
    r = yield from asyncio.sleep(3)
    print(r)
    print('hello again')

# 获取event loop
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()