# icmp_receiver.py
from scapy.all import *

def is_packet(packet):
    if packet.haslayer(ICMP) and packet[IP].ttl == 1:
        packet.show()

def receive_packet():
    sniff(filter="icmp", prn=is_packet, count=1)

if __name__ == "__main__":
    receive_packet()
