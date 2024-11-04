from scapy.all import IP, ICMP, send

# Implement your ICMP sender here
def sender():
    packet = IP(dst = "receiver", ttl=1)/ICMP() 
    send(packet)


if __name__ == "__main__":
    sender()
