# Project Euler Problem 21

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

def pd_sum(n):
    """returns sum of proper divisors of n"""   
    unproper = divs(n)
    unproper.sort(reverse=True)
    proper = unproper[1:]
    return sum(proper)

amicables = []

for a in range(1,10000):
    d_a = pd_sum(a)
    b = d_a
    d_b = pd_sum(b)
    
    if b != a:
        if d_a == b and d_b == a:
            amicables.append(a)
                 
print(f'Ans = {sum(amicables)}')
