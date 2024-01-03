import threading
import subprocess
import socket

def socket_iperf():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('163.22.22.79', 5602))
    data = client.recv(1024)
    print(f"Received: {data.decode()}")
    print(f"Please wait for at least 10 seconds")
    subprocess.run(['iperf3', '-c', '163.22.22.79', '-p', str(data.decode())], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("Thanks for testing!")
    client.close()

socket_iperf()
