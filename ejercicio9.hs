distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (p0, p1, p2) (q0, q1, q2) = abs (p0 - q0) + abs (p1 - q1) + abs (p2 - q2) 

distanciaManhattan2 :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan2 (p0, p1, p2) (q0, q1, q2) = sum [abs (p-q) | (p, q) <- zip [0..2] [0..2]]

main :: IO ()
main = print (distanciaManhattan2 (2, 3, 4) (7, 3, 8))

