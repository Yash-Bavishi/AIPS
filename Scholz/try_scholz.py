#!/bin/python3
import threading
import sys
import socket
import multiprocessing

ip_address = str(sys.argv[1])
port = 100
def process1(ip):
    def thread1(ip):
        def sub_thread1(ip):
            for i in range(0,512):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(i)
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread2(ip):
            for i in range(513,1024):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread3(ip):
            for i in range(1025,1536):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread4(ip):
            for i in range(1537,2048):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread5(ip):
            for i in range(2049,2560):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread6(ip):
            for i in range(2560,3072):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread7(ip):
            for i in range(3073,3584):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread8(ip):
            for i in range(3585,4096):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        thread1 = threading.Thread(target=sub_thread1, args=(ip,))
        thread1.start()
        thread2 = threading.Thread(target=sub_thread2, args=(ip,))
        thread2.start()
        thread3 = threading.Thread(target=sub_thread3, args=(ip,))
        thread3.start()
        thread4 = threading.Thread(target=sub_thread4, args=(ip,))
        thread4.start()
        thread5 = threading.Thread(target=sub_thread5, args=(ip,))
        thread5.start()
        thread6 = threading.Thread(target=sub_thread6, args=(ip,))
        thread6.start()
        thread7 = threading.Thread(target=sub_thread7, args=(ip,))
        thread7.start()
        thread8 = threading.Thread(target=sub_thread8, args=(ip,))
        thread8.start()
    def thread2(ip):
        def sub_thread1(ip):
            for i in range(4097,4608):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread2(ip):
            for i in range(4609,5120):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread3(ip):
            for i in range(5121,5632):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread4(ip):
            for i in range(5633,6144):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread5(ip):
            for i in range(6145,6656):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread6(ip):
            for i in range(6657,7168):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread7(ip):
            for i in range(7169,7680):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread8(ip):
            for i in range(7681,8192):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        thread1 = threading.Thread(target=sub_thread1, args=(ip,))
        thread1.start()
        thread2 = threading.Thread(target=sub_thread2, args=(ip,))
        thread2.start()
        thread3 = threading.Thread(target=sub_thread3, args=(ip,))
        thread3.start()
        thread4 = threading.Thread(target=sub_thread4, args=(ip,))
        thread4.start()
        thread5 = threading.Thread(target=sub_thread5, args=(ip,))
        thread5.start()
        thread6 = threading.Thread(target=sub_thread6, args=(ip,))
        thread6.start()
        thread7 = threading.Thread(target=sub_thread7, args=(ip,))
        thread7.start()
        thread8 = threading.Thread(target=sub_thread8, args=(ip,))
        thread8.start()
    def thread3(ip):
        def sub_thread1(ip):
            for i in range(8193,8704):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread2(ip):
            for i in range(8705,9216):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread3(ip):
            for i in range(9217,9728):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread4(ip):
            for i in range(9729,10240):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread5(ip):
            for i in range(10241,10752):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread6(ip):
            for i in range(10753,11264):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread7(ip):
            for i in range(11265,11776):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread8(ip):
            for i in range(11777,12288):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        thread1 = threading.Thread(target=sub_thread1, args=(ip,))
        thread1.start()
        thread2 = threading.Thread(target=sub_thread2, args=(ip,))
        thread2.start()
        thread3 = threading.Thread(target=sub_thread3, args=(ip,))
        thread3.start()
        thread4 = threading.Thread(target=sub_thread4, args=(ip,))
        thread4.start()
        thread5 = threading.Thread(target=sub_thread5, args=(ip,))
        thread5.start()
        thread6 = threading.Thread(target=sub_thread6, args=(ip,))
        thread6.start()
        thread7 = threading.Thread(target=sub_thread7, args=(ip,))
        thread7.start()
        thread8 = threading.Thread(target=sub_thread8, args=(ip,))
        thread8.start()
    def thread4(ip):
        def sub_thread1(ip):
            for i in range(12289,12800):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread2(ip):
            for i in range(12801,13312):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread3(ip):
            for i in range(13313,13824):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread4(ip):
            for i in range(13825,14336):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread5(ip):
            for i in range(14337,14848):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread6(ip):
            for i in range(14849,15360):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread7(ip):
            for i in range(15361,15872):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread8(ip):
            for i in range(15873,16384):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        thread1 = threading.Thread(target=sub_thread1, args=(ip,))
        thread1.start()
        thread2 = threading.Thread(target=sub_thread2, args=(ip,))
        thread2.start()
        thread3 = threading.Thread(target=sub_thread3, args=(ip,))
        thread3.start()
        thread4 = threading.Thread(target=sub_thread4, args=(ip,))
        thread4.start()
        thread5 = threading.Thread(target=sub_thread5, args=(ip,))
        thread5.start()
        thread6 = threading.Thread(target=sub_thread6, args=(ip,))
        thread6.start()
        thread7 = threading.Thread(target=sub_thread7, args=(ip,))
        thread7.start()
        thread8 = threading.Thread(target=sub_thread8, args=(ip,))
        thread8.start()
    thread1(ip)
    thread2(ip)
    thread3(ip)
    thread4(ip)
def process2(ip):
    def thread1(ip):
        def sub_thread1(ip):
            for i in range(16385,16896):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread2(ip):
            for i in range(16897,17408):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread3(ip):
            for i in range(17409,17920):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread4(ip):
            for i in range(17921,18432):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread5(ip):
            for i in range(18433,18944):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread6(ip):
            for i in range(18945,19456):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread7(ip):
            for i in range(19457,19968):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread8(ip):
            for i in range(19968,20480):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        thread1 = threading.Thread(target=sub_thread1, args=(ip,))
        thread1.start()
        thread2 = threading.Thread(target=sub_thread2, args=(ip,))
        thread2.start()
        thread3 = threading.Thread(target=sub_thread3, args=(ip,))
        thread3.start()
        thread4 = threading.Thread(target=sub_thread4, args=(ip,))
        thread4.start()
        thread5 = threading.Thread(target=sub_thread5, args=(ip,))
        thread5.start()
        thread6 = threading.Thread(target=sub_thread6, args=(ip,))
        thread6.start()
        thread7 = threading.Thread(target=sub_thread7, args=(ip,))
        thread7.start()
        thread8 = threading.Thread(target=sub_thread8, args=(ip,))
        thread8.start()
    def thread2(ip):
        def sub_thread1(ip):
            for i in range(20481,20992):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread2(ip):
            for i in range(20993,21504):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread3(ip):
            for i in range(21505,22016):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread4(ip):
            for i in range(22017,22528):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread5(ip):
            for i in range(22529,23040):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread6(ip):
            for i in range(23041,23552):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread7(ip):
            for i in range(23553,24064):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread8(ip):
            for i in range(24065,24576):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        thread1 = threading.Thread(target=sub_thread1, args=(ip,))
        thread1.start()
        thread2 = threading.Thread(target=sub_thread2, args=(ip,))
        thread2.start()
        thread3 = threading.Thread(target=sub_thread3, args=(ip,))
        thread3.start()
        thread4 = threading.Thread(target=sub_thread4, args=(ip,))
        thread4.start()
        thread5 = threading.Thread(target=sub_thread5, args=(ip,))
        thread5.start()
        thread6 = threading.Thread(target=sub_thread6, args=(ip,))
        thread6.start()
        thread7 = threading.Thread(target=sub_thread7, args=(ip,))
        thread7.start()
        thread8 = threading.Thread(target=sub_thread8, args=(ip,))
        thread8.start()
    def thread3(ip):
        def sub_thread1(ip):
            for i in range(24577,25088):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread2(ip):
            for i in range(25089,25600):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread3(ip):
            for i in range(25601,26112):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread4(ip):
            for i in range(26113,26624):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread5(ip):
            for i in range(26625,27136):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread6(ip):
            for i in range(27137,27648):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread7(ip):
            for i in range(27649,28160):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread8(ip):
            for i in range(28161,28672):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        thread1 = threading.Thread(target=sub_thread1, args=(ip,))
        thread1.start()
        thread2 = threading.Thread(target=sub_thread2, args=(ip,))
        thread2.start()
        thread3 = threading.Thread(target=sub_thread3, args=(ip,))
        thread3.start()
        thread4 = threading.Thread(target=sub_thread4, args=(ip,))
        thread4.start()
        thread5 = threading.Thread(target=sub_thread5, args=(ip,))
        thread5.start()
        thread6 = threading.Thread(target=sub_thread6, args=(ip,))
        thread6.start()
        thread7 = threading.Thread(target=sub_thread7, args=(ip,))
        thread7.start()
        thread8 = threading.Thread(target=sub_thread8, args=(ip,))
        thread8.start()
    def thread4(ip):
        def sub_thread1(ip):
            for i in range(28673,29184):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread2(ip):
            for i in range(29185,29696):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread3(ip):
            for i in range(29697,30208):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread4(ip):
            for i in range(30209,30720):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread5(ip):
            for i in range(30721,31232):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread6(ip):
            for i in range(31233,31744):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread7(ip):
            for i in range(31745,32256):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread8(ip):
            for i in range(32257,32768):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        thread1 = threading.Thread(target=sub_thread1, args=(ip,))
        thread1.start()
        thread2 = threading.Thread(target=sub_thread2, args=(ip,))
        thread2.start()
        thread3 = threading.Thread(target=sub_thread3, args=(ip,))
        thread3.start()
        thread4 = threading.Thread(target=sub_thread4, args=(ip,))
        thread4.start()
        thread5 = threading.Thread(target=sub_thread5, args=(ip,))
        thread5.start()
        thread6 = threading.Thread(target=sub_thread6, args=(ip,))
        thread6.start()
        thread7 = threading.Thread(target=sub_thread7, args=(ip,))
        thread7.start()
        thread8 = threading.Thread(target=sub_thread8, args=(ip,))
        thread8.start()
    thread1(ip)
    thread2(ip)
    thread3(ip)
    thread4(ip)
def process3(ip):
    def thread1(ip):
        def sub_thread1(ip):
            for i in range(32769,33280):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread2(ip):
            for i in range(33281,33792):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread3(ip):
            for i in range(33793,34304):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread4(ip):
            for i in range(34305,34816):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread5(ip):
            for i in range(34817,35328):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread6(ip):
            for i in range(35329,35840):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread7(ip):
            for i in range(35841,36352):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread8(ip):
            for i in range(36353,36864):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        thread1 = threading.Thread(target=sub_thread1, args=(ip,))
        thread1.start()
        thread2 = threading.Thread(target=sub_thread2, args=(ip,))
        thread2.start()
        thread3 = threading.Thread(target=sub_thread3, args=(ip,))
        thread3.start()
        thread4 = threading.Thread(target=sub_thread4, args=(ip,))
        thread4.start()
        thread5 = threading.Thread(target=sub_thread5, args=(ip,))
        thread5.start()
        thread6 = threading.Thread(target=sub_thread6, args=(ip,))
        thread6.start()
        thread7 = threading.Thread(target=sub_thread7, args=(ip,))
        thread7.start()
        thread8 = threading.Thread(target=sub_thread8, args=(ip,))
        thread8.start()
    def thread2(ip):
        def sub_thread1(ip):
            for i in range(36865,37376):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread2(ip):
            for i in range(37377,37888):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread3(ip):
            for i in range(37889,38400):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread4(ip):
            for i in range(38401,38912):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread5(ip):
            for i in range(38913,39424):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread6(ip):
            for i in range(39425,39936):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread7(ip):
            for i in range(39937,40448):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread8(ip):
            for i in range(40449,40960):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        thread1 = threading.Thread(target=sub_thread1, args=(ip,))
        thread1.start()
        thread2 = threading.Thread(target=sub_thread2, args=(ip,))
        thread2.start()
        thread3 = threading.Thread(target=sub_thread3, args=(ip,))
        thread3.start()
        thread4 = threading.Thread(target=sub_thread4, args=(ip,))
        thread4.start()
        thread5 = threading.Thread(target=sub_thread5, args=(ip,))
        thread5.start()
        thread6 = threading.Thread(target=sub_thread6, args=(ip,))
        thread6.start()
        thread7 = threading.Thread(target=sub_thread7, args=(ip,))
        thread7.start()
        thread8 = threading.Thread(target=sub_thread8, args=(ip,))
        thread8.start()
    def thread3(ip):
        def sub_thread1(ip):
            for i in range(40961,41472):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread2(ip):
            for i in range(41473,41984):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread3(ip):
            for i in range(41985,42496):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread4(ip):
            for i in range(42497,43008):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread5(ip):
            for i in range(43009,43520):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread6(ip):
            for i in range(43521,44032):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread7(ip):
            for i in range(44033,44544):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread8(ip):
            for i in range(44545,45056):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        thread1 = threading.Thread(target=sub_thread1, args=(ip,))
        thread1.start()
        thread2 = threading.Thread(target=sub_thread2, args=(ip,))
        thread2.start()
        thread3 = threading.Thread(target=sub_thread3, args=(ip,))
        thread3.start()
        thread4 = threading.Thread(target=sub_thread4, args=(ip,))
        thread4.start()
        thread5 = threading.Thread(target=sub_thread5, args=(ip,))
        thread5.start()
        thread6 = threading.Thread(target=sub_thread6, args=(ip,))
        thread6.start()
        thread7 = threading.Thread(target=sub_thread7, args=(ip,))
        thread7.start()
        thread8 = threading.Thread(target=sub_thread8, args=(ip,))
        thread8.start()
    def thread4(ip):
        def sub_thread1(ip):
            for i in range(45057,45568):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread2(ip):
            for i in range(45569,46080):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread3(ip):
            for i in range(46081,46592):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread4(ip):
            for i in range(46593,47104):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread5(ip):
            for i in range(47105,47616):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread6(ip):
            for i in range(47617,48128):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread7(ip):
            for i in range(48129,48640):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread8(ip):
            for i in range(48641,49152):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        thread1 = threading.Thread(target=sub_thread1, args=(ip,))
        thread1.start()
        thread2 = threading.Thread(target=sub_thread2, args=(ip,))
        thread2.start()
        thread3 = threading.Thread(target=sub_thread3, args=(ip,))
        thread3.start()
        thread4 = threading.Thread(target=sub_thread4, args=(ip,))
        thread4.start()
        thread5 = threading.Thread(target=sub_thread5, args=(ip,))
        thread5.start()
        thread6 = threading.Thread(target=sub_thread6, args=(ip,))
        thread6.start()
        thread7 = threading.Thread(target=sub_thread7, args=(ip,))
        thread7.start()
        thread8 = threading.Thread(target=sub_thread8, args=(ip,))
        thread8.start()
    thread1(ip)
    thread2(ip)
    thread3(ip)
    thread4(ip)
def process4(ip):
    def thread1(ip):
        def sub_thread1(ip):
            for i in range(49153,49664):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread2(ip):
            for i in range(49665,50176):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread3(ip):
            for i in range(50177,50688):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread4(ip):
            for i in range(50689,51200):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread5(ip):
            for i in range(51201,51712):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread6(ip):
            for i in range(51713,52224):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread7(ip):
            for i in range(52225,52736):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread8(ip):
            for i in range(52737,53248):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        thread1 = threading.Thread(target=sub_thread1, args=(ip,))
        thread1.start()
        thread2 = threading.Thread(target=sub_thread2, args=(ip,))
        thread2.start()
        thread3 = threading.Thread(target=sub_thread3, args=(ip,))
        thread3.start()
        thread4 = threading.Thread(target=sub_thread4, args=(ip,))
        thread4.start()
        thread5 = threading.Thread(target=sub_thread5, args=(ip,))
        thread5.start()
        thread6 = threading.Thread(target=sub_thread6, args=(ip,))
        thread6.start()
        thread7 = threading.Thread(target=sub_thread7, args=(ip,))
        thread7.start()
        thread8 = threading.Thread(target=sub_thread8, args=(ip,))
        thread8.start()
    def thread2(ip):
        def sub_thread1(ip):
            for i in range(53249,53760):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread2(ip):
            for i in range(53761,54272):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread3(ip):
            for i in range(54273,54784):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread4(ip):
            for i in range(54785,55296):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread5(ip):
            for i in range(55297,55808):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread6(ip):
            for i in range(55809,56320):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread7(ip):
            for i in range(56321,56832):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread8(ip):
            for i in range(56833,57344):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        thread1 = threading.Thread(target=sub_thread1, args=(ip,))
        thread1.start()
        thread2 = threading.Thread(target=sub_thread2, args=(ip,))
        thread2.start()
        thread3 = threading.Thread(target=sub_thread3, args=(ip,))
        thread3.start()
        thread4 = threading.Thread(target=sub_thread4, args=(ip,))
        thread4.start()
        thread5 = threading.Thread(target=sub_thread5, args=(ip,))
        thread5.start()
        thread6 = threading.Thread(target=sub_thread6, args=(ip,))
        thread6.start()
        thread7 = threading.Thread(target=sub_thread7, args=(ip,))
        thread7.start()
        thread8 = threading.Thread(target=sub_thread8, args=(ip,))
        thread8.start()
    def thread3(ip):
        def sub_thread1(ip):
            for i in range(57345,57856):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread2(ip):
            for i in range(57857,58368):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread3(ip):
            for i in range(58369,58880):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread4(ip):
            for i in range(58881,59392):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread5(ip):
            for i in range(59393,59904):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread6(ip):
            for i in range(59905,60416):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread7(ip):
            for i in range(60417,60928):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread8(ip):
            for i in range(60929,61440):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        thread1 = threading.Thread(target=sub_thread1, args=(ip,))
        thread1.start()
        thread2 = threading.Thread(target=sub_thread2, args=(ip,))
        thread2.start()
        thread3 = threading.Thread(target=sub_thread3, args=(ip,))
        thread3.start()
        thread4 = threading.Thread(target=sub_thread4, args=(ip,))
        thread4.start()
        thread5 = threading.Thread(target=sub_thread5, args=(ip,))
        thread5.start()
        thread6 = threading.Thread(target=sub_thread6, args=(ip,))
        thread6.start()
        thread7 = threading.Thread(target=sub_thread7, args=(ip,))
        thread7.start()
        thread8 = threading.Thread(target=sub_thread8, args=(ip,))
        thread8.start()
    def thread4(ip):
        def sub_thread1(ip):
            for i in range(61441,61952):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread2(ip):
            for i in range(61953,62464):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread3(ip):
            for i in range(62465,62977):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread4(ip):
            for i in range(62978,63488):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread5(ip):
            for i in range(63489,64000):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread6(ip):
            for i in range(64001,64512):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread7(ip):
            for i in range(64513,65024):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        def sub_thread8(ip):
            for i in range(65052,65536):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((ip,i))
                    print(str(i) + " Port is open")
                except ConnectionRefusedError:
                    pass
        thread1 = threading.Thread(target=sub_thread1, args=(ip,))
        thread1.start()
        thread2 = threading.Thread(target=sub_thread2, args=(ip,))
        thread2.start()
        thread3 = threading.Thread(target=sub_thread3, args=(ip,))
        thread3.start()
        thread4 = threading.Thread(target=sub_thread4, args=(ip,))
        thread4.start()
        thread5 = threading.Thread(target=sub_thread5, args=(ip,))
        thread5.start()
        thread6 = threading.Thread(target=sub_thread6, args=(ip,))
        thread6.start()
        thread7 = threading.Thread(target=sub_thread7, args=(ip,))
        thread7.start()
        thread8 = threading.Thread(target=sub_thread8, args=(ip,))
        thread8.start()
    thread1(ip)
    thread2(ip)
    thread3(ip)
    thread4(ip)


process1 = multiprocessing.Process(target=process1, args=(ip_address,))
process1.start()
process2 = multiprocessing.Process(target=process2, args=(ip_address,))
process2.start()
process3 = multiprocessing.Process(target=process3, args=(ip_address,))
process3.start()
process4 = multiprocessing.Process(target=process4, args=(ip_address,))
process4.start()
print("done")

