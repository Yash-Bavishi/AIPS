#!/bin/python3
"""

Author: Yash Bavishi & Saurabh Upadhyay
Date: 7 April 2021

"""

""" Algo

User -> IP -> Perform tcp_port scan

"""

import sys
import socket


if len(sys.argv) < 2:
    print('''Please Provide IP and PORT
eg: python3 tcp_scanner.py <ip_address> <port>''')
    sys.exit(1)


ip_addr = str(sys.argv[1])
port = int(sys.argv[2])
for i in range(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip_addr,i))
        sock.shutdown(2)
        print(str(i) + "Port is open")
    except ConnectionRefusedError:
        continue 
