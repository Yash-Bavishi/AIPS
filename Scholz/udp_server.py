#!/bin/python3

"""
Author: Yash Bavishi & Saurabh Upadhyay
Date 7 April 2021
"""

"""
Algo 

SERVER

"""

import socket 

ip_address = "127.0.0.1"
port = 8000

server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock.bind((ip_address, port))

while True:
    data, addr = server_sock.recvfrom(1024)
    print("Message: ", str(data))
    send_data = b'Hello Client'
    server_sock.sendto(send_data, addr)
    print("MEssage send")
