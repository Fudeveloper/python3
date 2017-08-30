from threading import Thread
import socket


# 收数据
def receive_data(udp_socket):
    while True:
        receive_info = udp_socket.recvfrom(1024)
        print(receive_info)


# 发数据
def send_data(udp_socket, send_addr,send_port):
    send_info = input('<<')
    udp_socket.sendto(send_info.encode('utf-8'), (send_addr, send_port))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('', 9998))
    send_addr = input("对方ip\n")
    send_port = int(input('对方port\n'))
    ts = Thread(target=send_data, args=(udp_socket, send_addr, send_port))
    tr = Thread(target=receive_data, args=(udp_socket, ))
    ts.start()
    tr.start()
    ts.join()
    tr.join()
if __name__ == '__main__':
    main()