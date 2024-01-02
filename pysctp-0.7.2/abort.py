import scapy.all as s
from Vtag import vtag
from sctp import *
import struct
#casue=1, invalid stream identifier
data = struct.pack('=BBHI', 0x06, 0x00, 0x0800, 0x04000700)
#(type, chunk flag, length, cause code, cause)
pkt = s.IP(dst="10.22.24.236")/s.SCTP(dport=65432, sport=65432, tag=vtag)/data

client_sock = sctpsocket(socket.AF_INET, socket.SOCK_STREAM, None)

print(pkt.dst)
print(pkt.ttl)
print(repr(pkt))
pkt.show()
s.send(pkt)
