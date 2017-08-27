def start():
    data = ''       # 存储的作用，data始终为空
    r = yield data
    print('1',r)
    r = yield data
    print('2',r)
    r = yield data
    print('3',r)
    r = yield data   # 最后一个为空代表结束

gen = start()
gen.send(None)
gen.send('a')
gen.send('b')
gen.send('c')


