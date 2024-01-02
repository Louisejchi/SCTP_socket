import _sctp
from sctp import *

import time

# 建立 socket 物件
client_socket = sctpsocket(socket.AF_INET, socket.SOCK_STREAM, None)

# 連線至 server 端
client_socket.connect(('10.22.24.106', 65432))

# 發送 5 個訊息
for i in range(5):
    message = f'M {i+1}'
    client_socket.sctp_send(message.encode())
    print(f'Sent: {message}')

    try:
        # 設定超時時間為 10 秒
        client_socket.settimeout(10)
        data = client_socket.sctp_recv(1024)
    except socket.timeout:
        print('Timeout. No response from server for 10 seconds.')
        break

    print(f'Received: {data.decode()}')

# 關閉連線
client_socket.close()
