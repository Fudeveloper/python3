# 生产者
def maker(deleter):
    deleter.send(None)
    # maker_receive_value = ''
    maker_send_value =0
    while  maker_send_value < 10:
        maker_send_value += 1
        print('生产', maker_send_value)
        maker_receive_value = deleter.send(maker_send_value)
        print('消费者返回的', maker_receive_value)

    deleter.close()

# 消费者
def deleter():
    deleter_send_value = ''
    while True:
        deleter_receive_value = yield deleter_send_value
        if not deleter_receive_value:
            return
        print('消费', deleter_receive_value)
        deleter_send_value = 'OK' + str(deleter_receive_value)

gen = deleter()

maker(gen)