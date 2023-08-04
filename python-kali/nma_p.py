import nmap

def scan_network(target):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-T4 -F')  # Fast scan with timing level 4
    print(nm.all_hosts())
    for host in nm.all_hosts():
        print(f"Host: {host}, State: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            open_ports = nm[host][proto].keys()
            for port in open_ports:
                print(f"Port: {port}, State: {nm[host][proto][port]['state']}")

if __name__ == "__main__":
    target_ip = "172.31.3.181"  # Change this to your target network
    scan_network(target_ip)

