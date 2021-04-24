#!/bin/python3

import threading
import multiprocessing
import socket
ip = "127.0.0.1"

start = 1
end = 65535
def process1(ip,start,end):
    def thread1(ip,start,end):
        def sub(ip,start,end):
            for i in range(start,end):
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print("port is open " + str(i))
                except ConnectionRefusedError:
                    pass
        thread1 = threading.Thread(target=sub,args=(ip,start,end))
        thread1.start()
    thread1(ip,start,end)
for i in range(start,end):
    process1 = multiprocessing.Process(target=process1,args=(ip,start,start+512))
    process1.start()
