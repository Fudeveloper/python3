import socket
def main():
    dest = ('<broadcast>', 8081)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 允许udp_socet进行广播
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    udp_socket.sendto('hah'.encode('utf-8'), dest)
    udp_socket.close()

if __name__ == '__main__':
    main()