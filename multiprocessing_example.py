import multiprocessing
import time
import numpy as np
import concurrent.futures

def summ(n):
  result = 0
  for i in range (1,n+1):
    result += i
   return(f'summ({n}) = {result}')
   
print("Number of Cores: " + str(multiprocessing.cpu_count())

start = time.time()

with concurrent.futures.ProcessPoolExecutor() as executor:
  x = [1,2,3,4,5,6,7,8,9,10]
  results = executor.map(summ, x)
  for f in concurrent.futures.as_completed(results):
    print(f.result())
    
end = time.time()

print("Multiprocessing took: " + str(end-start) + " seconds!")
