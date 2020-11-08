# Project Euler Problem 40

constant = ''

i = 1
while len(constant) < 1000000:
    constant += str(i); i += 1;
    
ans = 1
for i in range(7):
    ans *= int(constant[((10**i)-1)])
    
print(f'Ans = {ans}')
