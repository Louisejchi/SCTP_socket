import _sctp
from Vtag import vtag
from sctp import *

server = '10.22.24.106'
sctpport = 65432

client_sock = sctpsocket(socket.AF_INET, socket.SOCK_STREAM, None)

saddr = (server, sctpport)

cport = 2904

# 設定連線超時時間為 10 秒
client_sock.settimeout(10)

try:
    client_sock.connect(saddr)
except socket.timeout:
    print('Timeout. Could not connect to the server in 10 seconds.')
    client_sock.close()
    exit()

data = "Hi"
client_sock.sctp_send(data)
try:
    data = client_sock.sctp_recv(1024)
except socket.timeout:
    print('Timeout. No response from server for 10 seconds.')
    client_sock.close()
    exit()
except BlockingIOError:
    print('BlockingIOError. The socket is not ready for the operation.')
    client_sock.close()
    exit()
