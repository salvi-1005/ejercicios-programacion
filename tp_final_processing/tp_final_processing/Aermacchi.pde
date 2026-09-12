class Aermacchi extends ElementoJuego {
  int vida = 3;
  int cadenciaDisparo = 300;
  int tiempoUltimoDisparo = 0;

  Aermacchi(float x, float y) {
    super(x, y, 40, 50, 5);
  }

  void actualizar() {
  }

  void mover(String direccion) {
    if (direccion.equals("izquierda")) x -= velocidad;
    if (direccion.equals("derecha")) x += velocidad;
    if (direccion.equals("arriba")) y -= velocidad;
    if (direccion.equals("abajo")) y += velocidad;

    x = constrain(x, 0, width - ancho);
    y = constrain(y, 0, height - alto);
  }

  boolean puedeDisparar() {
    return millis() - tiempoUltimoDisparo >= cadenciaDisparo;
  }

  ProyectilAliado disparar() {
    tiempoUltimoDisparo = millis();
    return new ProyectilAliado(x + ancho / 2 - 4, y);
  }

  void recibirImpacto(int danio) {
    vida -= danio;
    if (vida <= 0) {
      morir();
    }
  }

  boolean estaDestruido() {
    return vida <= 0;
  }

  void morir() {
    desactivar();
  }

  void dibujar() {
    fill(0, 180, 255);
    triangle(x + ancho / 2, y, x, y + alto, x + ancho, y + alto);
  }
}
