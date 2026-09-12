class BateriaEnemiga extends Enemigo {

  int tiempoUltimoDisparo;
  int cadenciaDisparo;

  BateriaEnemiga(float x, float y) {
    super(x, y, 45, 45, 1.5, 2, 200);
    tiempoUltimoDisparo = 0;
    cadenciaDisparo = 2000;
  }

  void actualizar() {
    mover();

    if (y > height) {
      desactivar();
    }

    if (puedeDisparar()) {
      ProyectilEnemigo proyectil = disparar();
      juego.elementos.add(proyectil);
    }
  }

  void mover() {
    y += velocidad;
  }

  boolean puedeDisparar() {
    return millis() - tiempoUltimoDisparo >= cadenciaDisparo;
  }

  ProyectilEnemigo disparar() {
    tiempoUltimoDisparo = millis();
    return new ProyectilEnemigo(x + ancho / 2 - 4, y + alto);
  }

  void dibujar() {
    fill(150, 80, 255);
    rect(x, y, ancho, alto);
  }
}
