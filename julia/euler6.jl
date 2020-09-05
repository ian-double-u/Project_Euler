# Project Euler Problem 6

println("Ans = ", abs((cumsum([i for i=1:100])[end])^2 - cumsum([i^2 for i=1:100])[end]))
