import socket
import sctp

# 建立 SCTP socket 物件
client_socket = sctp.sctpsocket_tcp(socket.AF_INET)

# 連線至 server 端
client_socket.connect(('10.22.24.106', 5600))

# 傳送訊息至 server 端
message = 'Hello, Server!'
client_socket.sendall(message.encode())

# 接收 server 端回應
data = client_socket.recv(1024)
print(f'Received from server: {data.decode()}')

# 關閉連線
client_socket.close()

