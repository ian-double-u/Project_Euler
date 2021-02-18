from itertools import permutations  

def make_string(tuple_):
    result = ''
    for i in range(len(tuple_)):
        result += tuple_[i]
    return result
    
def solve(n,m):
    set_ = [str(i) for i in range(n)]
    lex = []
    for i in permutations(set_):
        lex.append(make_string(i))
    lex.sort()
    print(f'Ans = {lex[m-1]}')
    
solve(10,1000000)
