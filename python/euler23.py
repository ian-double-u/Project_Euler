abundant_nums = []

def abundant(x):
    y = sum([i for i in range(1,x) if x%i==0])
    if y > x:
        return True
    else:
        return False    
        
for num in range(1,28124):
    if abundant(num):
        abundant_nums.append(num)
        
two_abundant_nums = [i+j for i in abundant_nums for j in abundant_nums]

print(f'Ans = {sum(list(range(1,28124)))-sum(list(set(list(range(1,28124))) & set(two_abundant_nums)))}')
