# Project Euler Problem 2

fib = [1,2]

def term(a,b): 
    f = a + b
    return f

while fib[-1] < 4000000:
    fib.append(term(fib[-2],fib[-1]))
    
fib.remove(fib[-1])

sum = 0
for f in fib:
    if f%2 == 0:
        sum += f
        
print(f'Ans = {sum}')
