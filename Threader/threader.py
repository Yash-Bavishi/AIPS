#!/bin/python3 

import threading
import time 
import socket 


def print_hello():
    for i in range(21):
        if i == 10:
            time.sleep(2)
        print("Hello")
def print_number(number):
    for i in range(number + 1):
    print(i)


thread1 = threading.Thread(target = print_hello, args = () )
thread1.start()
thread2 = threading.Thread(target = print_number, args = (10,))
#thread1.start()
thread2.start()
thread2.join()
print("This is the main thread")
#thread1.join()

print("This is the main thread again")
print("Thread1 and Thread2 have finished executing")
