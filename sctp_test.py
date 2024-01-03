import threading
import subprocess
import socket
from sctp import *

def socket_iperf():
    client = sctpsocket_tcp(socket.AF_INET)
    client.settimeout(10)
    print(f"Please wait for at least 10 seconds")
    try:
        client.connect(('163.22.22.79', 12123))
        data = client.recv(1024)
        print(f"Received: {data.decode()}")
        subprocess.run(['iperf3', '-c', '163.22.22.79', '-p', str(data.decode()), '--sctp'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except socket.timeout:
        print("No data received in 10 seconds, closing connection")
    finally:
        print("Thanks for testing!")
        client.close()

socket_iperf()
