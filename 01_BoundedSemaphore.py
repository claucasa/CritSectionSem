# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:39:05 2022

@author: claud
"""

from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array

from  multiprocessing import BoundedSemaphore
N=8

def task(sem,common,tid):
    for i in range(100):
        sem.acquire()
        try:
           print(f'{tid}-{i}:Critical section')
           v = common.value +1
           print(f'{tid}-{i}: Inside critical section')
           common.value = v
           print(f'{tid}-{i}: End of critical section')
        finally:
            sem.release()

def main():
    lp=[]
    common = Value('i',0)
    sem= BoundedSemaphore(1)
    for tid in range(N):
        lp.append(Process(target=task,args=(sem,common,tid)))
    print(f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
        
    for p in lp:
        p.join()
    print(f'Valor final del contador {common.value}')
    print('fin')
if __name__  == "__main__":
    main()
    