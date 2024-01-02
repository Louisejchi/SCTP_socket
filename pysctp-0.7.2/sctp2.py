import sctp
import socket

server_sock = sctp.sctpsocket_udp(socket.AF_INET)

server_sock.bind(("0.0.0.0", 1234))
server_sock.listen()
conn, addr = server_sock.accept()
while True:
    conn_sock.recv(1024)
