# main.py
from firewall import check_connection


ip_address = input("Enter an IP address: ")
port = int(input("Enter a port number: "))

check_connection(ip_address, port)