# Project Euler Problem 5

global test_num = 1

while true
    println(test_num)
    bool = [test_num%i for i=11:20]

    if cumsum(bool)[end] == 0
        println("Ans = ", test_num)
        break
    end

    global test_num += 1
end
