library(readxl)
library(tidyverse)

#1)
tapply(lluvia_pampa$mar[lluvia_pampa$año<2000],
       lluvia_pampa$localidad[lluvia_pampa$año<2000],sum)

lluvia_pampa %>%
  filter(año<2000) %>%
  group_by(localidad) %>%
  summarise(total_marzo = sum(mar))

#2)
sim_normal <- function(n,mu,s) {
  datos<-rnorm(n, mu, s)
  par(mfrow = c(1, 3))
  hist(datos, main = "histograma", xlab = "datos", ylab = "frecuency")
  dn <- density(datos)
  lines(dn, lwd = 2, col = "red")
  plot(dn, lwd = 2, col = "red", main = "densidad")
  rug(jitter(datos))
  boxplot(datos, main = "boxplot", horizontal = FALSE)
  par(mfrow = c(1, 1))
  (valores<- c(n,mu,s))
  print(valores)
}

#3)
set.seed(7) `
edad<- sample(20:45, 20, replace = T)  
sexo<- sample(c("M", "F"), 20, replace = T) 
lugar<-sample(c("capital", "provincia"), 20, replace = T)

#promedio de la edad por sexo:
g <- data_frame(edad, sexo, lugar)
tapply(g$edad[g$lugar == "capital"], g$sexo[g$lugar == "capital"],mean)
tapply(g$edad[g$lugar == "provincia"], g$sexo[g$lugar == "provincia"],mean)

#promedio de la edad por lugar:
g <- data_frame(edad, sexo, lugar)
tapply(g$edad[g$sexo == "M"], g$lugar[g$sexo == "M"],mean)
tapply(g$edad[g$sexo == "F"], g$lugar[g$sexo == "F"],mean)
