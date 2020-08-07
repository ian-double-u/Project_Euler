for i in range(1,1000): # i = a
    for j in range(1,1000): # j = b
        for k in range(1,1000): # k = c
            if (i+j+k == 1000):
                if (i**2 + j**2 == k**2):
                    print(f'Ans = {i*j*k}')
                    break
