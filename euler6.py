# Project Euler Problem 6

sum_of_squares, square_of_sum = 0,0

for i in range(1,101):
    sum_of_squares += i**2
    square_of_sum += i

print(f'Ans = {((square_of_sum)**2)-sum_of_squares}')
