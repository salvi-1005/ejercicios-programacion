class ProyectilEnemigo extends Proyectil {
  ProyectilEnemigo(float x, float y) {
    super(x, y, 5, 1);
  }

  void actualizar() {
    mover();
    if (estaFueraDePantalla()) desactivar();
  }

  void mover() {
    y += velocidad;
  }

  void dibujar() {
    fill(255, 0, 0);
    rect(x, y, ancho, alto);
  }
}
