import threading
import socket
import subprocess
import re
from sctp import *
from concurrent.futures import ThreadPoolExecutor

port = 5400
executor = ThreadPoolExecutor(max_workers=100)

def handle_client(conn, addr):
    global port
    print(f"Handling connection from {addr}")
    conn.sendall(str(port).encode())
    print(port)
    port += 1
    conn.close()

    # iperf3
    process = subprocess.Popen(['iperf3', '-s', '-p', str(port)], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    # output file
    with open('iperf_sctp_output.txt', 'a') as f:
        f.write(output.decode())

def start_server():
    server = sctpsocket_tcp(socket.AF_INET)
    server.bind(('0.0.0.0', 12111))
    server.listen()
    print("Server is listening...")
    while True:
        conn, addr = server.accept()
        executor.submit(handle_client, conn, addr)

sctp_thread = threading.Thread(target=start_server)
sctp_thread.start()
