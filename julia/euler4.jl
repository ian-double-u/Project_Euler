# Project Euler Problem 4

function pal_test(num)
    # num is string
    digits = [parse(Int,i) for i=split(num, "")]
    r_digits = reverse(digits)
    check = [abs(digits[i]-r_digits[i]) for i=1:size(digits)[1]]

    if cumsum(check)[end] == 0
        return true
    else
        return false
    end
end

println("Ans = ", findmax([parse(Int,i) for i=[string(i*j) for i=100:999 for j=100:999] if pal_test(i)==true])[1])
