# Project Euler Problem 25

fib = [1,2]

def term(a,b): 
    f = a + b
    return f

while len(str(fib[-1])) < 1000:
    fib.append(term(fib[-2],fib[-1]))
    
print(f'Ans = {len(fib)+1}')
