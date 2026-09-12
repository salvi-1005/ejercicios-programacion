d <- base
d %>%
  is.na()

#1)
  -persona_id
  -año
  -edad
  -gran_area_descripcion
  -area_descripcion
  -disciplina_descripcion
  -sexo

#2)Sí, hay datos faltantes. Se verifican con la funcion is.na()

#3)
d %>%
  group_by(gran_area_descripcion) %>%
  summarize(promedio_edad = mean(edad, na.rm =T), desvio_edad = sd(edad, na.rm = T))

#4)
d %>%
  filter(gran_area_descripcion == "HUMANIDADES") %>%
  select(edad, gran_area_descripcion)

#5)
write.table(x = edad, file = "base", sep = ",", row.names = FALSE, col.names = TRUE)

#6)
hist(base$edad)

#7)
boxplot(base$edad)
  
#8)
es_masculino <- filter(d, sexo == "Masculino") 
hist(es_masculino$edad)

#9)
despues_de_2013 <- filter(d, anio > 2012)
boxplot(despues_de_2013$edad)

#10)
par(mfrow = c(2, 2))

#gráfico 1
hist(base$edad)

#gráfico 2
boxplot(base$edad)

#gráfico 3
es_masculino <- filter(d, sexo == "Masculino") 
hist(es_masculino$edad)

#gráfico 4
despues_de_2013 <- filter(d, anio > 2012)
boxplot(despues_de_2013$edad)



