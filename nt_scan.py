import socket

def scan_port(target_ip, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for the connection attempt
        s.settimeout(1)
        
        # Attempt to connect to the target IP address and port
        result = s.connect_ex((target_ip, port))
        
        # Check the result of the connection attempt
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed or filtered")
        
        # Close the socket connection
        s.close()
    
    except socket.error as e:
        print(f"Error: {e}")

def network_scan(target_ip):
    print(f"Scanning {target_ip}...\n")
    
    # Define a list of common ports to scan
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445]
    
    # Iterate over the common ports and scan each one
    for port in common_ports:
        scan_port(target_ip, port)

if __name__ == "__main__":
    target_ip = input("Enter the target IP address to scan: ")
    network_scan(target_ip)

