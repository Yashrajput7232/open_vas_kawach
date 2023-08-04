import socket

def scan_network(start_ip, end_ip):
    active_hosts = []

    # Convert the start and end IP addresses to integers for iteration
    start_int = int(''.join(f'{int(x):02}' for x in start_ip.split('.')))
    end_int = int(''.join(f'{int(x):02}' for x in end_ip.split('.')))

    for ip_int in range(start_int, end_int + 1):
        # Convert the integer back to IP address format
        ip_address = '.'.join(str((ip_int >> (8 * i)) & 255) for i in range(3, -1, -1))
        
        try:
            # Try to establish a connection to the host
            socket.setdefaulttimeout(1)  # Set the socket timeout to 1 second
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((ip_address, 80))
            active_hosts.append(ip_address)
        except:
            pass

    return active_hosts

if __name__ == "__main__":
    start_ip = "172.31.0.0"
    end_ip = "172.31.3.182"

    hosts = scan_network(start_ip, end_ip)
    if len(hosts) > 0:
        print("Active hosts in the network:")
        for host in hosts:
            print(host)
    else:
        print("No active hosts found in the network.")
