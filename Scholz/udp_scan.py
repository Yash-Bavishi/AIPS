#!/bin/python3

import socket
import sys


message = b'Hello server'
ip = str(sys.argv[1])
port = int(sys.argv[2])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    try:
        sock.sendto(message,(ip,port))
        sock.settimeout(5)
        data, addr = sock.recvfrom(1024)
        if (data  != None):
            print(data)
            sys.exit(1)
    except socket.timeout:
        print("port is probably closed")
        sys.exit(1)
