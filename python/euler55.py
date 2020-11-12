# Project Euler Problem 55

def palindrome_test(x):    
    digits = [int(i) for i in list(str(x))]
    check_list = [abs(digits[i] - digits[-(i+1)]) for i in range(len(digits))]
    
    if sum(check_list) == 0:
        return True
    else:
        return False
        
def digit_flip(x):
    digits = [i for i in list(str(x))]
    digits.reverse()
    return int(''.join(digits))
    
lychrel = []

for n in range(10,10000):
    count = 0
    for i in range(50):
        if palindrome_test(n+digit_flip(n)):
            count += 1
        
        n = n+digit_flip(n)
        
    if count == 0:
        lychrel.append(n)
        
print(f'Ans = {len(lychrel)}')
