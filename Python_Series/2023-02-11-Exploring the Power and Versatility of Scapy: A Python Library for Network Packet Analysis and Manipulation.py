# Scapy is a powerful and versatile Python library for manipulating and analyzing network packets.
# Here is an example of how to use Scapy to capture and analyze packets on a network:
from scapy.all import *

# Capture packets on the network
packets = sniff(iface="eth0", count=10)

# Print packet information
for packet in packets:
    print(packet.summary())
    print(packet.show())