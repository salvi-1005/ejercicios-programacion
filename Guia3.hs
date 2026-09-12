f :: Int -> Int
f n | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16
absoluto :: Int -> Int
absoluto x | x < 0 = x * (-1)
           | x >= 0 = x
maximoabsoluto :: Int -> Int -> Int
maximoabsoluto x y | abs x > abs y = abs x
                   | abs x < abs y = abs y
maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z | (x > y) && (y > z) = x
              | (x > z) && (z > y) = x
              | (y > x) && (x > z) = y
              | (y > z) && (z > x) = y
              | (z > x) && (x > y) = z
              | (z > y) && (y > x) = z
algunoEs0 :: Int -> Int -> Bool
algunoEs0 x y | x == 0 = True
              | y == 0 = True
              | (x /= 0) && (y /= 0) = False
ambosSon0 :: Int -> Int -> Bool
ambosSon0 x y | (x == 0) && (y == 0) = True
              | x /= 0 = False
              | y /= 0 = False
mismoIntervalo :: Int -> Int -> Bool
mismoIntervalo x y | (x <= 3) && (y <= 3) = True
                   | (x > 7) && (y > 7) = True
                   | ((x > 3) && (y > 3)) && ((x <= 7) && (y <= 7)) = True
                   | otherwise = False
sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z | (x /= y) && (y /= z) && (x /= z) = x + y + z

esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y | mod x y == 0 = True
                 | otherwise = False

digitoUnidades :: Int -> Int
digitoUnidades x = div x 10

digitoDecenas :: Int -> Int
digitoDecenas x = div x 100

estanRelacionados :: Int -> Int -> Bool
estanRelacionados x y | x*x + x*y*k == 0 = True
                              where k /= 0
                      | otherwise = False

                     