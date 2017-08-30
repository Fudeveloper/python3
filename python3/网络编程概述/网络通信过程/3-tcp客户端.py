import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connect_address = ()
client_socket.connect(('172.26.144.1', 8888))

# 发数据
client_socket.send('123'.encode('utf-8'))

# 收数据
recive_data = client_socket.recv(1024)
print(recive_data)

client_socket.close()
