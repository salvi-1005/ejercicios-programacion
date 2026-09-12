mi.promedio <- function(x) {
  L = length(x)
  P = sum(x)/L
  return(P)
}

mi.primera.funcion <- function(x, y = 3) {
  p = x + y
  return(p)
}

mi.primera.funcion <- function(x = c(2,3,4), y = 3) {
  p <- rep(NA, length(x))
  for( i in 1:length(x)){
    p[i] <- x[i] + y
}

return(p)
}

i <- 1
while(i <= length(x)) {
  p[i] <- x[i] + y
  i <- i + 1
}
return(p)

promedios <- function(d, nombre.col){
  pepe <- d %>% 
  select({(nombre.col)}) %>%
  summarize(p = mean({{nombre.col}}, na.rm = T))
  return(pepe)
}

library(dplyr)

set.seed(1010)
aux = rchisq(100, df=2)

dfEstudiantes = tibble(legajo = paste0("LE_",1:100), 
                       edad = as.integer((80-18) * aux/max(aux) + 18),
                       carrera = sample(c("Ciencias Físicas",
                                          "Ciencias Matemáticas",
                                          "Ciencias de Datos",
                                          "Paleontología",
                                          "Ciencias Biológicas",
                                          "Ciencias de la Atmósfera",
                                          "Ciencias de la Computación",
                                          "Ciencias Geológicas",
                                          "Ciencias Químicas",
                                          "Ciencia y Tecnología de Alimentos",
                                          "Oceanografía"),
                                        100, replace = T))

dfNotas = rbind(tibble(legajo = sample(paste0("LE_",1:50),30),
                       nota = as.integer(runif(30,min=2,max=10)),
                       materia = "Biología"),
                tibble(legajo = sample(paste0("LE_",1:100),50),
                       nota = as.integer(runif(50,min=2,max=10)),
                       materia = "Matemática"))

#1.1)
  dfEstudiantes %>%
+ inner_join(dfNotas, by = "legajo") %>%
+ filter(materia == "Biología") %>%
+ group_by(carrera) %>%
+ summarise(promedio = mean(nota))
 #1.2) 
  dfEstudiantes %>%
+ left_join(dfNotas, dfEstudiantes, by = "legajo") %>% 
+ filter(is.na(nota)) %>%
+ group_by(carrera) %>%
+ summarise(cant = n())
  #1.3)
  dfEstudiantes %>%
+ inner_join(dfNotas, by = "legajo") %>%
+ select(legajo, edad) %>%
+ distinct() %>%
+ summarise(promEdad = mean(edad), cant = n())
  #1.4)
  dfEstudiantes %>%
+ mutate(edadCat = cut_number(edad,3)) %>%
+ inner_join(dfNotas, by = "legajo") %>%
+ group_by(materia, edadCat)
+ ggplot(aes(x = edadCat, y = nota, color = materia)) + geom_boxplot()
  #2.1)
  rango <- function(x) {
    p <- range(x)
    return(p)
  }
  #2.2)
  mi.promedio <- function(x) {
    L = length(x)
    P = sum(x)/L
    return(P)
  }
  #2.3)
  cantidad.de.na <- function(x) {
    p <- count(q)
    q <- is.na(x) 
    return(p)
  }
  #2.4)
  cambiar.na.por.uno <- function(x) {
    p <- (x)
    NA <- 1
    return(p)
  }
  #2.6)
  redondear <- function(x) {
    p <- round(x / sum(x, na.rm = TRUE) * 100, 1)
    return(p)
  }
  #2.7)
  ambos.na <- function(x, y)
    for( i in 1:length(x))
      x[i] = na
    for( j in 1:length(y))
      y[j] = na
  return(i, j)
  #2.9)
  f2 <- function(lst, n) {
    length(lst) >= n
  }
  