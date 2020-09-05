# Project Euler Problem 5

n = 20
while True:
    bool = [n%i for i in range(11,21)]
    
    if sum(bool) == 0:
        print(f'Ans = {n}')
        break
    
    n += 1
