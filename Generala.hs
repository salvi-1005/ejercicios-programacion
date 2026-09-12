import GHC.Base (BCO, TrName (TrNameD))
generala :: [Int] -> Int
generala (x:y:xs) | todosIguales (x:y:xs) = 55
                  | esPermutacion (x:y:xs) (xs:x:y) && cantidadDeApariciones x == 2 && cantidadDeApariciones y == 3 = 35
                  | esPermutacion (x:y:xs) (xs:x:y) && cantidadDeApariciones x == 1 && cantidadDeApariciones y == 4 = 45
                  | min == 1 && max == 6 && estaOrdenada (x:y:xs) = 25
                  | otherwise = 0

todosIguales :: [Int] -> Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x:y:xs) = x == y && todosIguales (y:xs)

estaOrdenada :: [Int] -> Bool
estaOrdenada [] = True
estaOrdenada [x] = True
estaOrdenada (x:y:xs) = x < y && estaOrdenada (y:xs)

esPermutacion :: [Int] -> [Int] -> Bool
esPermutacion [] [] = True
esPermutacion (x:xs) (y:ys) | mismosElementos (x:xs) (y:ys) = True
                            | otherwise = False

mismosElementos :: [t] -> [t] -> Bool
mismosElementos xs ys = contenido xs ys && contenido ys xs

contenido :: [a] -> [a] -> Bool
contenido [] _ = True
contenido (x:xs) ys = x `elem` ys && contenido xs ys

cantidadDeApariciones :: [Int] -> Int -> Int
cantidadDeApariciones [] x = 0
cantidadDeApariciones (y:xs) x | not (pertenece x (y:xs)) = 0
                               | otherwise = y : (cantidadDeApariciones xs x)

pertenece :: (Eq a) => a -> [a] -> Bool
pertenece e [] = False
pertenece e (x:xs) | e == x = True 
                   | otherwise = pertenece e xs