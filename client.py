import socket
import sctp

# SCTP socket 
client_socket = sctp.sctpsocket_tcp(socket.AF_INET)

# 設定連線超時時間為 10 秒
client_socket.settimeout(10)

try:
    # connect server
    print('Wait for a maximum of 10 seconds...')
    client_socket.connect(('163.22.22.79', 12457))
except socket.timeout:
    print('Timeout. Could not connect to the server in 10 seconds.')
    print('Thanks for testing!!')
    client_socket.close()
    exit()

# 輸入測試者所在地
print('----------------------------')
message = input("請輸入所在地址: ")
client_socket.sendall(message.encode())

try:
    print('Wait for a maximum of 10 seconds...')
    data = client_socket.recv(1024)
except socket.timeout:
    print('Timeout. No response from server for 10 seconds.')
    print('Thanks for testing!!')
    client_socket.close()
    exit()

print('----------------------------')
print('Thanks for testing!!')
print(f'Received: {data.decode()}')

# disconnect
client_socket.close()
