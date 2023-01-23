import time
def fib(n):
   fi = [0] * (n+1) 
   fi[1] = 1
   for i in range (2,n+1): 
      fi[i] = fi[i-1] + fi[i-2] 
   return fi[n]
start = time.time()
end = time.time()
fibvalue=fib(34)
print("fib(34)= ",fibvalue)
print("fib(34) took {} seconds".format(end-start) )