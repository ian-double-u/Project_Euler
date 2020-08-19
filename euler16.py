# Project Euler Problem 16

def digits(x): 
    """returns digits of x"""
    
    if type(x) != int: 
        print("ERROR <- x in factorial(x) is not type int")
        return
    
    return [int(i) for i in list(str(x))]

print(f'Ans = {sum(digits(2**1000))}')
