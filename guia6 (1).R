

library(palmerpenguins)

ggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g)) +
geom_point()

modelo_regresion <- lm(body_mass_g ~ flipper_length_mm, data = penguins)
#coeficientes
coef(modelo_regresion)
#obtener los coeficientes del modelo
beta_0 <- coef(modelo_regresion)[1]
pendiente <- coef(modelo_regresion)[2]
#Crear el resumen de un modelo
resumen <- summary(modelo_regresion)

ggplot(na.omit(penguins), aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_point() +
  geom_abline(intercept = beta_0, slope = pendiente, color = "red") +
  ggtitle("recta de regresion lineal") +
  theme_minimal()
# X = peso corporal, Y = longitud de las aletas
nuevas_longitudes_aletas <- data.frame(flipper_length_mm = seq(180, 240, by = 10))
nuevas_predicciones <- predict(modelo_regresion, newdata = nuevas_longitudes_aletas)
nuevos_datos <- cbind(nuevas_longitudes_aletas, Prediccion_Peso = nuevas_predicciones)

ggplot(na.omit(penguins), aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_point() +
  geom_abline(intercept = beta_0, slope = pendiente, color = "red") +
  ggtitle("recta de regresion lineal") +
  geom_point(data = nuevos_datos, aes(x = flipper_length_mm, y = Prediccion_Peso))
  theme_minimal()
  
  
#1.2)
  d <- penguins
  e <- filter(d, species == "Adelie") 
    ggplot(na.omit(e), aes(x = bill_depth_mm, y = bill_length_mm)) +
    geom_point()
#1.3)
  modelo_regresion_lineal_adelie <- lm(bill_length_mm ~ bill_depth_mm, data = e)
#1.4)
  coef(modelo_regresion_lineal_adelie)
  beta_0 <- coef(modelo_regresion_lineal_adelie)[1]
  pendiente <- coef(modelo_regresion_lineal_adelie)[2]
#1.5)
  residuals(modelo_regresion_lineal_adelie)
  mean(residuals(modelo_regresion_lineal_adelie)**2)
#1.6)
  modelo_regresion_lineal_adelie <- lm(bill_length_mm == 24 ~ bill_depth_mm == 0, data = c)
  modelo_regresion_lineal_adelie <- lm(bill_length_mm ~ bill_depth_mm == 5, data = c)
  
  largo_pico <- data.frame(bill_depth_mm = 20)
  nuevas_predicciones_pico <- predict(modelo_regresion_lineal_adelie, newdata = largo_pico)
  nuevos_datos_pico <- cbind(largo_pico, prediccion_largo_pico = nuevas_predicciones_pico)
  
  ancho_pico <- data.frame(bill_depth_mm = 5)
  nuevas_predicciones_pico <- predict(modelo_regresion_lineal_adelie, newdata = ancho_pico)
  nuevos_datos_pico <- cbind(ancho_pico, prediccion_ancho_pico = nuevas_predicciones_pico)
#1.7)
  e <- filter(d, species == "Adelie")
  modelo_regresion_lineal_adelie <- lm(bill_length_mm ~ bill_depth_mm, data = d)
  
  g <- filter(d, species == "Gentoo")
  modelo_regresion_lineal_gentoo <- lm(bill_length_mm ~ bill_depth_mm, data = g)
  
  h <- filter(d, species == "Chinstrap")
  modelo_regresion_lineal_chinstrap <- lm(bill_length_mm ~ bill_depth_mm, data = h)
#1.8)
  ggplot(data = penguins, mapping = aes(x = bill_depth_mm, y = bill_length_mm, color = species)) +
    geom_point() +
    geom_smooth(method = "lm")

  ggplot(na.omit(d), aes(x = bill_depth_mm, y = bill_length_mm)) +
    geom_point() +
    geom_abline(intercept = beta_0, slope = pendiente, shape = "red") +
    geom_point(data = g, aes(x = bill_depth_mm, y = bill_length_mm)) +
    theme_minimal()
#1.9)
  c <- na.omit(d) 
  promedio <- (c %>%
  filter(species == "Adelie") %>%
  summarize(bill_depth_promedio = mean(bill_depth_mm)))

  c %>%
  filter(species == "Adelie") %>%
  summarize(bill_length_promedio = mean(bill_length_mm))
  #largo = 2 x ancho

  mean(residuals(modelo_regresion_lineal_adelie)**2)
  var_obs <- var(flipper_length_mm)
  var_pred <- var(predict(modelo_regresion_lineal_adelie))
  r_cuadrado <- var_pred/var_obs
  
  d <- na.omit(penguins)
  flipper_length_mm <- select(d, flipper_length_mm)
  