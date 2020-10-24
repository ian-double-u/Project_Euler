# Project Euler Problem 29

def unique_powers(a,b):
    return len(list(set([x**y for x in range(2,a+1) for y in range(2,b+1)])))

print(unique_powers(100,100))
