# Project Euler Problem 7

n = 1000000
A = [1 for i=1:n]

for i=2:(Int(sqrt(n))+1) # Sieve of Eratosthenes
    if A[i] == 1
        j = i^2
        while j < n
            A[j] = 0
            j += i
        end
    end
end

A = A[2:end]

prime_count = 0
num = 1 # start at 1 since removed 1 from A

for i=A
    global num += 1
    if i==1
        global prime_count += 1
    end
    if prime_count == 10001
        println("Ans = ", num)
        break
    end
end
