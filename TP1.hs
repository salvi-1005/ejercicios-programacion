esPrimo :: Integer -> Integer -> Bool
esPrimo n a | a == n = True
            | mod n a == 0 = False
            | otherwise = esPrimo n (a + 1)

divisorcomun :: Integer -> Integer -> Integer -> Bool
divisorcomun a b n | n > a = False
                   | n > b = False
                   | mod a n == 0 && mod b n == 0 = True
                   | otherwise = divisorcomun a b (n + 1)

esCoprimo :: Integer -> Integer -> Bool
esCoprimo a b | esPrimo a 2 == True && esPrimo b 2 == True = True
              | divisorcomun a b 2 == False = True
              | otherwise = False
              
aPseudo :: Integer -> Integer -> Bool
aPseudo n a | mod (a^(n-1) - 1) n == 0 = True
            | otherwise = False              
            
f :: Integer -> Integer -> Bool
f n a | a == 1 = True
      | esCoprimo n a == False = f n (a - 1)
      | aPseudo n a == True = f n (a - 1)
      | otherwise = False

esCarmichael :: Integer -> Bool
esCarmichael n | f n (n - 1) == True = True
               | otherwise = False 

