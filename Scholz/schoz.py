#!/bin/python

import sys
import socket

if(len(sys.argv) < 2):
    print("Please provide ip address and port ")
    sys.exit(1)

ip = str(sys.argv[1])
port = int(sys.argv[2])
for i in range(port + 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip,i))
        sock.shutdown(1)
        print(str(i) + " is open")
    except ConnectionRefusedError:
        pass
