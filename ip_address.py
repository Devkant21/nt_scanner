import socket

def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    ip_address = get_ip_address()
    if ip_address:
        print("Your IP address is:", ip_address)
