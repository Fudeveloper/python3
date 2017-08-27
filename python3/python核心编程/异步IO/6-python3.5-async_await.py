import asyncio
import time
async def hello():
    print('hello world')
    await hello2()
    print('hello end')

async def hello2():
    print('hello2')
    await asyncio.sleep(5)
    print('hello2end')

async def hello3():
    print('hello3')
    await asyncio.sleep(10)
    print('hello3end')
loop = asyncio.get_event_loop()
tasks = [hello(),hello2(),hello3()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()