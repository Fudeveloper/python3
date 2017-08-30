import socket

server_socket = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
# 设置套接字为非堵塞
server_socket.setblocking(False)

bind_addr = ('', 8888)
server_socket.bind(bind_addr)

# 设置套接字为监听（被动）套接字
server_socket.listen(5)

# 用来保存所有已连接客户端信息
client_addr_list = []
while True:
    try:
        client_socket, client_addr = server_socket.accept()
    except:
        pass
    else:
        #
        client_socket.setblocking(False)
        print('新的客户端{0}'.format(client_addr))
        client_addr_list.append((client_socket, client_addr))

    for client_socket, client_addr in client_addr_list:
        try:
            recv_data = client_socket.recv(1024)
        except:
            pass
        else:
            if len(recv_data ) > 0:
                print('{0}'.format(str(recv_data)))
            else:
                client_socket.close()
                client_addr_list.remove((client_socket, client_addr))
                print('{0}已下线'.format(client_addr))
