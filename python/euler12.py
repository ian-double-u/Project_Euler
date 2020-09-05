# Project Euler Problem 12

def t_n(n):
    """returns n-th triangular number"""
    list = [i for i in range(0,n+1)]
    return sum(list)

def divs(t):
    """returns list of divisors for
    a natural number t"""
    divisors = []
    d = 1   # divisor
    f = t/d # dividend
    
    while d <= f:
        if t%d == 0:           # if d is a divisor
            divisors.append(d) # add divisor,
            divisors.append(f) # and dividend to list of divisors
            
        d += 1
        
    return list(set(divisors))

n = 1
d = 0

while True:
    if n%2 == 0:
        k = n/2
        d += (len(divs(k))*len(divs(2*k+1)))
        
    else:
        k = (n-1)/2
        d += (len(divs(k+1))*len(divs(2*k+1)))
        
    if d >= 500:
        print(f'Ans = {t_n(n)}')
        break
    
    else:
        d = 0
        n += 1
