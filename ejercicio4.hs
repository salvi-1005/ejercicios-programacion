sumaImpares :: Integer -> Integer
sumaImpares 0 = 0
sumaImpares 1 = 1
sumaImpares x = (2*x - 1) + sumaImpares (x-1) 
              

main :: IO ()
main = print (sumaImpares 3)         