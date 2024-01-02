import threading
import socket
import subprocess
import re
from sctp import *
from concurrent.futures import ThreadPoolExecutor

port = 5200
executor = ThreadPoolExecutor(max_workers=100)

def handle_client(conn, addr):
    global port
    print(f"Handling connection from {addr}")
    conn.send(str(port).encode())
    print(port)
    port += 1
    conn.close()

    # iperf3
    process = subprocess.Popen(['iperf3', '-s', '-p', str(port)], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    # output file
    with open('iperf_tcp_output.txt', 'a') as f:
        f.write(output.decode())

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5600))
    server.listen()
    print("Server is listening...")
    while True:
        conn, addr = server.accept()
        executor.submit(handle_client, conn, addr)

tcp_thread = threading.Thread(target=start_server)
tcp_thread.start()
