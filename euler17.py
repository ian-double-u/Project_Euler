# Project Euler Problem 17

ones = ['one','two','three','four','five','six','seven','eight','nine']
teens = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen',
         'seventeen','eighteen','nineteen']
tens = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty',
        'ninety']

letters = 0

letters += len('onethousand')
for i in range(1,1000):
    num_str = ''
    
    if i > 99:
        hundreds_place = int(str(i)[0])
        tens_place = int(str(i)[1])
        ones_place = int(str(i)[2])
        
        num_str += ones[hundreds_place-1]
        num_str += 'hundredand'
        
        if tens_place == 0:
            if ones_place != 0:
                num_str += ones[ones_place-1]
                
            else:
                letters -= 3
        
        elif tens_place == 1:
            
            if ones_place == 0:
                num_str += tens[0]
            
            else:
                num_str += teens[ones_place-1]
        
        else:            
            num_str += tens[tens_place-1]
        
            if ones_place != 0:
                num_str += ones[ones_place-1]
    
    elif i < 100 and i > 19:
        tens_place = int(str(i)[0])
        ones_place = int(str(i)[1])
        
        num_str += tens[tens_place-1]
        
        if ones_place != 0:
            num_str += ones[ones_place-1]
    
    elif i < 20 and i > 10:
        num_str += teens[i-11]
    
    elif i == 10:
        num_str += tens[0]
    
    else: 
        num_str += ones[i-1]
    
    print(num_str)
    letters += len(num_str)
    
print(f'Ans = {letters}')
