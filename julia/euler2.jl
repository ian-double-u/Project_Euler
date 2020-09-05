function next_fib(a,b)
    return a+b
end

fib_seq = [1,2]

while next_fib(fib_seq[end-1],fib_seq[end]) < 4000000
    push!(fib_seq,next_fib(fib_seq[end-1],fib_seq[end]))
end

println("Ans = ", cumsum([i for i=fib_seq if i%2==0])[end])
