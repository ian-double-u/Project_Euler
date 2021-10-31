nextFib :: [Integer] -> [Integer]
nextFib f = f ++ [((reverse f) !! 0) + ((reverse f) !! 1)]

ans = foldl (+) 0 (filter even (last (takeWhile (\x -> last x < 4000000) (iterate nextFib [1,2]))))
