import sys
from scapy.all import IP, ICMP, TCP, sr1

def network_scan(target_ip, timeout=2):
    print(f"Scanning {target_ip}...")
    try:
        # Send ICMP echo request (ping) to the target IP
        icmp = IP(dst=target_ip)/ICMP()
        resp = sr1(icmp, timeout=timeout, verbose=False)

        if resp is not None:
            print(f"{target_ip} is online")
            # Send TCP SYN packet to common ports
            for port in range(1, 1025):  # Scan common ports (1-1024)
                tcp_pkt = IP(dst=target_ip)/TCP(dport=port, flags='S')
                resp = sr1(tcp_pkt, timeout=timeout, verbose=False)
                if resp and resp.haslayer(TCP) and resp.getlayer(TCP).flags == 0x12:  # SYN-ACK
                    print(f"Port {port} is open")
            print("Scan complete")
        else:
            print(f"{target_ip} is offline")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python network_scan.py <target_ip>")
        sys.exit(1)

    target_ip = sys.argv[1]
    network_scan(target_ip)
