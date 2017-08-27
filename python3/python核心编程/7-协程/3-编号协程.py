def start():
    for i in range(100000):
        r = yield i
        print(i,r)

gen = start()
gen.send(None)
gen.send('wang')
gen.send('liu')

# 0 wang
# 1 liu