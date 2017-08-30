import socket

# tcp
# socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# udp
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

send_addr = ('172.26.144.1', 8080)
send_data = '123'.encode('utf-8')
udp_socket.sendto(send_data, send_addr)