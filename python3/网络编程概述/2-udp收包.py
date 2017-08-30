import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bind_addr = ('', 7789)
udp_socket.bind(bind_addr)
recv_data = udp_socket.recvfrom(1024)
print(recv_data)
# send_addr = ('172.26.144.1', 7786)
# udp_socket.sendto('123'.encode('utf-8'),send_addr)
udp_socket.close()

