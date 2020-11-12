def sieve_of_Eratosthenes(n): # returns all primes under n
    A = [True]*n
    for i in range(2,int(n**(0.5))+1): 
        if A[i] == True:
            j = i**2
            while j < n:
                A[j] = False
                j += i                  
    return [i for i in range(len(A)) if A[i] == True][2:]
