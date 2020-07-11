import numpy as np

n = 110000
A = [True]*n
    
for i in range(2,int(np.sqrt(n))+1): # Sieve of Eratosthenes
    if A[i] == True:
        j = i**2
        while j < n:
            A[j] = False
            j += i

counter = []
for z in range(0,len(A)):
    if A[z] == True:
        counter.append(z)
    
print(f'Ans = {counter[10002]}') # counts 0 and 1 for some reason
