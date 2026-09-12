library(palmerpenguins)
d <- na.omit(penguins)
#1)
#A) peso = alfa + largo de la aleta*beta1 + sexo*beta2
#B)
fit <- lm(body_mass_g ~ flipper_length_mm + sex, data = d)
coef(fit)
mean(residuals(fit)**2)
var_obs = var(body_mass_g)
var_pred = var(predict(fit))
r_cuadrado = nueva_prediccion/nuevo_peso
#C)
ggplot(data = d, aes(x = flipper_length_mm, y = body_mass_g, color = sex)) +
  geom_point() +
  geom_abline(intercept = -4013, slope = 40.6) +
  geom_abline(intercept = -3513, slope = 40.6) 
#D)La diferencia es beta_2, es decir, la ordenada al origen

#2)
#A)peso = alfa + largo de la aleta*beta1 + especie*beta2
#B)Se predice en funcion de la especie en vez del sexo
#C)
fit2 <- lm(body_mass_g ~ flipper_length_mm + species, data = d)
coef(fit2)
mean(residuals(fit2)**2)
#D)
ggplot(data = d, aes(x = flipper_length_mm, y = body_mass_g, color = species)) +
  geom_point() +
  geom_abline(intercept = -4013, slope = 40.6, color = "pink") +
  geom_abline(intercept = -3973, slope = 40.6, color = "blue") +
  geom_abline(intercept = -3933, slope = 40.6, color = "green") 

#3)
#A) peso = alfa + largo de la aleta*beta1 + especie*beta2 + (especie * largo de la aleta)*beta3
#B) Hay tres variables predictoras en vez de dos.
#C)
fit3 <- lm(body_mass_g ~ flipper_length_mm + species + flipper_length_mm*species, data = d)
coef(fit3)
mean(residuals(fit3)**2)
var_obs = var(body_mass_g)
var_pred = var(predict(fit3))
r_cuadrado = nueva_prediccion/nuevo_peso
#D)
ggplot(data = d, aes(x = flipper_length_mm, y = body_mass_g, color = species)) +
  geom_point() +
  geom_abline(intercept = -2508, slope = 32.68, color = "pink") +
  geom_abline(intercept = -2508-4166, slope = 32.68 + 21.47, color = "blue") +
  geom_abline(intercept = -2508-4166-529, slope = 32.68 + 21.47 + 1.88, color = "green")
#E)Se diferencia la pendiente y la ordenada al origen

#4)
#A)
dTrain = d[1:275,]
dTest = d[275:344,]
#B)
sample(1:275, replace = F, 220)
sample(275:344, replace = F, 68.8)
especie_train <- lm(body_mass_g ~ island + species, data = d[1:275,])
sexo_train <- lm(body_mass_g ~ island + sex + species, data = d[1:275,])
año_train <- lm(body_mass_g ~ island + sex + species + year, data = d[1:275,])
largo_aleta_train <- lm(body_mass_g ~ island + sex + species + year + flipper_length_mm, data = d[1:275,])
largo_pico_train <- lm(body_mass_g ~ island + sex + species + year + flipper_length_mm + bill_length_mm, data = d[1:275,])
ancho_pico_train <- lm(body_mass_g ~ island + sex + species + year + flipper_length_mm + bill_length_mm + bill_depth_mm, data = d[1:275,])

especie_test <- lm(body_mass_g ~ island + species, data = d[275:344,])
sexo_test <- lm(body_mass_g ~ island + sex + species, data = d[275:344,])
año_test <- lm(body_mass_g ~ island + sex + species + year, data = d[275:344,])
largo_aleta_test <- lm(body_mass_g ~ island + sex + species + year + flipper_length_mm, data = d[275:344,])
largo_pico_test <- lm(body_mass_g ~ island + sex + species + year + flipper_length_mm + bill_length_mm, data = d[275:344,])
ancho_pico_test <- lm(body_mass_g ~ island + sex + species + year + flipper_length_mm + bill_length_mm + bill_depth_mm, data = d[275:344,])

#C)
mean(residuals(especie_train)**2)
mean(residuals(sexo_train)**2)
mean(residuals(año_train)**2)
mean(residuals(largo_aleta_train)**2)
mean(residuals(largo_pico_train)**2)
mean(residuals(ancho_pico_train)**2)

mean(residuals(especie_test)**2)
mean(residuals(sexo_test)**2)
mean(residuals(año_test)**2)
mean(residuals(largo_aleta_test)**2)
mean(residuals(largo_pico_test)**2)
mean(residuals(ancho_pico_test)**2)
#D) Cuantas más variables predictoras hay, menos error de predicción hay