#!/bin/python3
import threading
import multiprocessing

total = 65535
no_of_process = 4
divide_processes = total//no_of_process + 1
print(divide_processes)
no_of_threads = 16
division_of_threads = divide_processes//no_of_threads 
print(division_of_threads)
k = 1
threads = 4
processor = 4
for i in range(processor):
    print("The processor number " + str(i + 1) )
    for j in range(threads):
        print("The threads number " + str(j + 1))
        for l in range(8):
            print("Port scanning will start from " + str(k))
            k = k + 512
            
print(k-1)


# each processor -> 4 threads
