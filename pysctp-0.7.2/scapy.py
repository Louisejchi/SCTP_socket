from scapy.all import *

ip = IP(dst="10.22.24.235")
sctp = SCTP(sport=7890, dport=7890)

chunk = SCTP_CHUNK_DATA(data="Hello")

packet = ip/sctp/chunk
send(packet)

