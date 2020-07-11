import numpy as np

n = 2000000
A = [True]*n
    
for i in range(2,int(np.sqrt(n))+1): # Sieve of Eratosthenes
    if A[i] == True:
        j = i**2
        while j < n:
            A[j] = False
            j += i        

sum = 0
for z in range(0,len(A)):
    if A[z] == True:
        sum += z
        
print(f'Ans = {sum-1}')
