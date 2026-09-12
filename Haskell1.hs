
{-}
main = do
       putStrLn "Greetings!  What is your name?"
       inpStr <- getLine
       putStrLn $ "Welcome to Haskell, " ++ reve inpStr ++ "!   " ++ toString (stringEq inpStr "hola")
       putStrLn $ aplanar [inpStr,reve inpStr]
-}
stringEq :: [Char] -> [Char] -> Bool
stringEq [] [] = True
stringEq (x:xs) (y:ys) = x == y && stringEq xs ys
stringEq _ _ = False


toString :: Bool -> [Char] 
toString x = if x then "True" else "False"


reve :: [t] -> [t]
reve [] = []
reve (x:xs) = reve xs ++ [x]


aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar [x] = x
aplanar (x:xs) = x ++ [' '] ++ aplanar xs


bbb :: ([Char],[Char]) -> Char -> [Char]
bbb ([],[]) _ = []
bbb ( x:xs , y:ys ) z = if x == z then [y] else bbb (xs,ys) z


buscar :: ([Char],[Char]) -> [Char] -> [Char]
buscar ([_],[_]) [] = []
buscar ( x , y ) [z] = bbb (x,y) z 
buscar ( x , y ) ( z:zs ) = bbb (x,y) z ++ buscar (x,y) (zs)


main = do
       let b0 = "1234"
       let b1 = "5678"
       let ce = "2391"
       putStrLn $ b0 ++ "  " ++ b1 ++ "  " ++ ce
       putStrLn $ buscar (b0,b1) ce

