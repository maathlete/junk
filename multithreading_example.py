#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:02:14 2020

@author: alexandra
"""

import multiprocessing
import time
import numpy as np

print("Number of Cores:" + str(multiprocessing.cpu_count()))

start = time.time()

for i in range(0,10):
    time.sleep(1)
    
end  = time.time()
print("Synchronous execution took: " + str(end-start) + str(" seconds"))

start = time.time()

def sleep(n):
    time.sleep(n)

pool = multiprocessing.Pool(4)
pool.map(sleep, [1 for i in range(0,10)])

end  = time.time()
print("Pooling took: " + str(round(end-start,2)) + str(" seconds"))

