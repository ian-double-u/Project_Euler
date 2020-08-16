# Project Euler Problem 14

def next_term(x):
    """returns next term in the Collatz Sequence given x"""
    if x%2 == 0:
        return x/2
    else:
        return 3*x + 1
    
def Collatz(seed):
    """generates Collatz sequence given seed"""
    
    sq = []
    
    while True:
        next_t = next_term(seed)
        
        if next_t == 1:
            sq.append(next_t)
            break
        
        else:
            sq.append(seed)
            seed = next_t
            
    return sq
        
seed_list = []
len_list = []

for i in range(1,1000000):
    seed_list.append(i)
    len_list.append(len(Collatz(i)))
        
max_len = max(len_list)

max_seeds = [i for i in range(0,len(len_list)) if len_list[i] == max_len]

print(f'Ans = {seed_list[max_seeds[-1]]}')
