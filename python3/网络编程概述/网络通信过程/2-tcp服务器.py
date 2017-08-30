import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 8899))
server_socket.listen(5)

# 如果有新的客户来连接服务器，那么就产生一个新的套接字专门为这个客户服务
client_socket, client_info = server_socket.accept()
recv_data = client_socket.recv(1024)
print(recv_data)

client_socket.close()
server_socket.close()