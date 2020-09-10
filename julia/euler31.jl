# Project Euler Problem 31

c = pushfirst!([0 for i=0:200],1)
for k=[1,2,5,10,20,50,100,200]
    for i=1:(201-k)
        c[i+k] += c[i]
    end
end
println("Ans = ", c[201])
