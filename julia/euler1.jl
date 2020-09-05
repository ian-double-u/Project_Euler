# Project Euler Problem 1

println("Ans = ", cumsum([i for i=1:999 if i%3==0 || i%5==0])[end])
