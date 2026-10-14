# firewall.py
blocked_ips = ["192.168.1.50"]
blocked_ports = [23, 445]


def check_connection(ip_address, port):
    print("\nChecking connection...")
    print(f"IP Address: {ip_address}")
    print(f"Port: {port}")

    if ip_address in blocked_ips:
        print("BLOCKED: IP address is on the blocklist.")
    elif port in blocked_ports:
        print("BLOCKED: Port is on the blocklist.")
    else:
        print("BLOCKED: Default rule triggered.")