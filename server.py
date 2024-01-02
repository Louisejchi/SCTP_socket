import socket
import sctp
import threading

#  SCTP socket
server_socket = sctp.sctpsocket_tcp(socket.AF_INET)

# bind
server_socket.bind(('0.0.0.0', 12345))

# listen
server_socket.listen()

print('Server is listening...')

def client(client_socket, addr):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f'Received from client: {data.decode()}')
        client_socket.sendall(data)
        # outputfile
        with open('client_ips.txt', 'a') as f:
            f.write(f'{addr[0]} : {data.decode()}\n')

while True:
    client_socket, addr = server_socket.accept()
    print(f'Connected by {addr}')
    # threading
    threading.Thread(target=client, args=(client_socket, addr)).start()
