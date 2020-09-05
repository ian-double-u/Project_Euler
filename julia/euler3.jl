# Project Euler Problem 3

function factor_list(num)
    f_l = []

    while num%2==0
        push!(f_l,2)
        num/=2
    end

    d = 3

    while d^2 <= num
        if num%d==0
            push!(f_l,d)
            num /= d
        else
            d += 2
        end
    end

    if num != 1
        push!(f_l, num)
    end

    return f_l
end

println("Ans = ", factor_list(600851475143)[end])
