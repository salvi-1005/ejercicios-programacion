library(readr)
library(dplyr)
require(tidyverse)
trips_2022_reducido <- read_csv("Descargas/trips_2022_reducido.csv")
View(trips_2022_reducido)
head(trips_2022_reducido)

library(readr)
export <- read_csv("Descargas/export.csv")
View(export)

d = trips_2022_reducido


filter(d, duracion_recorrido>300 & duracion_recorrido<3600)

"Es claro que los que mas usan las bicicletas son los hombres, luego las mujeres y por ultimo 'otros'"
ggplot(na.omit(d), aes(x=Género)) +
  geom_bar(stat="count")


"Deducir cual seria el objetivo de los viajes mas frecuentes y duracion de los mismos"
frecuentes=data.frame(d %>% 
                        group_by(nombre_estacion_origen,nombre_estacion_destino) %>% 
                        count() %>% 
                        arrange(desc(n)))

View(frecuentes)

frecuentes = data.frame(subset(frecuentes, n>10))
View(frecuentes)

"Nueva columna recorrido"
frecuentes=mutate(frecuentes,recorrido = paste(nombre_estacion_origen,nombre_estacion_destino,sep="-"))
View(frecuentes)

ggplot(na.omit(frecuentes), aes(x=n ,y = recorrido)) +
  geom_bar(stat="identity",color="blue",fill=rgb(0.1,0.4,0.5,0.7))

"Vemos los 5 recorridos mas frecuentes: Julieta Lanteri - Julieta Lanteri lidera el ranking.
Ubicada en Puerto Madero, probablemente el recorrido sea mas que nada con fines turisticos"

clima <- export
view(clima)
clima%>%
select(date, tavg)
ggplot(export, aes(x = date, y = tavg)) + 
  geom_line(linetype = "dashed") +
  geom_point()
#se puede ver que al principio y al principio y al final del año, la temperatura es mayor, y a mitad de año, es más baja.
clima%>%
select(date, prcp)
ggplot(export, aes(x = date, y = prcp)) + 
  geom_line(linetype = "dashed") +
  geom_point()
#A principio y a fin de año hay más lluvias, mientras que a mitad de año hay menos
usos.por.dia <- data.frame(d%>%
                            group_by(fecha) %>%
                            count())
usos.por.dia %>%
  ggplot(aes(x = fecha, y = n)) + 
  geom_line(linetype = "dashed") +
  geom_point()
#Se puede ver que en el otoño y en la primavera aumenta el uso de bicis, y en los fines de semana se usa menos que en los días de semana

