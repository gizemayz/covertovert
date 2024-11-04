from scapy.all import IP, ICMP, send

def sender():
    packet = IP(dst = "receiver", ttl=1)/ICMP() 
    send(packet)


if __name__ == "__main__":
    sender()
