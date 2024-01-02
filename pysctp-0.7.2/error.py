import scapy.all as s
from Vtag import vtag 
from sctp import *
import struct
#casue=1, invalid stream identifier
data = struct.pack('=BBHHHHH', 0x09, 0x00, 0x0c00, 0x0100, 0x0800, 0x1200, 0x0000)
#(type, chunk flag, length, cause code, cause)
pkt = s.IP(dst="10.22.24.236")/s.SCTP(dport=65432, sport=65432, tag=vtag)/data

print(pkt.dst)
print(pkt.ttl)
print(repr(pkt))
pkt.show()
s.send(pkt)
