import asyncio, datetime

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect          #这里不是生成器，只负责接收reader、writer
    print('reader={0},writer={1}'.format(reader,writer))
    print('*'*10, 2, '*'*10)
    header = 'GET / HTTP/1.0\r\nHost:%s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))  #header编码后写入了writer

    yield from writer.drain()           #这里是生成器 <generator object StreamWriter.drain at 0x02B20750>，这里生成了新的                                            header和body
    print(writer.drain)
    print('*'*10, 3, '*'*10)
    while True:
        line = yield from reader.readline() #只读取头部
        yield from asyncio.sleep(2)         #加入阻塞 否则看不出并行 打印的时候回sina sohu 163顺序打印
        print('*'*10, 4, '*'*10)
        if line == b'\r\n':
            break
        print('*'*10, 5, '*'*10)
        print('time: %s %s header > %s' %(datetime.datetime.now().strftime('%H:%M:%S.%f'), host, line.decode('utf-8').rstrip()))
        print('*'*10, 6, '*'*10)
     #Ignore the body, close the socket
        writer.close()
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com', 'www.sohu.com', 'www.163.com']]
print('*'*10, 1, '*'*10)
loop.run_until_complete(asyncio.wait(tasks))
print('*'*10, 7, '*'*10)
loop.close()