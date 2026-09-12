class CazaEnemigo extends Enemigo {
  CazaEnemigo(float x, float y) {
    super(x, y, 40, 40, 3, 1, 100);
  }

  void actualizar() {
    mover();
    if (y > height) desactivar();
  }

  void mover() {
    y += velocidad;
  }

  void dibujar() {
    fill(255, 80, 80);
    rect(x, y, ancho, alto);
  }
}
