# Project Euler Problem 3

def biggest_factor(x):
    pf = []
    
    while x % 2 == 0:
        pf.append(x)
        x /= 2

    y = 3

    while y*y <= x:
        if x % y == 0:
            pf.append(y)
            x /= y

        else:
            y += 2

    if x != 1:
        pf.append(x)
        
    return max(pf)

print(f'Ans = {int(biggest_factor(600851475143))}')
