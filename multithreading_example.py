#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:02:14 2020

@author: alexandra
"""

import multiprocessing
import time
import numpy as np

def sleep(n):
    time.sleep(n)

print("Number of Cores:" + str(multiprocessing.cpu_count()))

start = time.time()

for i in range(0,10):
    sleep(1)
    
end  = time.time()
print("Serial execution took: " + str(end-start) + str(" seconds"))

start = time.time()

pool = multiprocessing.Pool(4)
pool.map(sleep, [1 for i in range(0,10)])

end  = time.time()
print("Multithreading took: " + str(round(end-start,2)) + str(" seconds"))
