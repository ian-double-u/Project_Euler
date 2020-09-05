# Project Euler Problem 4

def digits(x): 
    """returns digits of x"""
    
    if type(x) != int: 
        print("ERROR <- x in factorial(x) is not type int")
        return
    
    return [int(i) for i in list(str(x))]

def palindrome_test(x):
    """returns True if x is a palindrome, False otherwise"""
    
    digits_list = digits(x)
    check_list = [abs(digits_list[i] - digits_list[-(i+1)]) for i in range(len(digits_list))]
    
    if sum(check_list) == 0:
        return True
    
    else:
        return False
    
products = [i*j for i in range(100,1000) for j in range(100,1000)]
pal_products = []

for i in products:
    if palindrome_test(i):
        pal_products.append(i)

pal_products.sort()
print(f'Ans = {pal_products[-1]}')    
