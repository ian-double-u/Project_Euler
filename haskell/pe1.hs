ans = foldl (+) 0 [i | i <- [1..999], (mod i 3) == 0 || (mod i 5) == 0]
