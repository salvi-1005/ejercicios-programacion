class ProyectilAliado extends Proyectil {
  ProyectilAliado(float x, float y) {
    super(x, y, -8, 1);
  }

  void actualizar() {
    mover();
    if (estaFueraDePantalla()) desactivar();
  }

  void mover() {
    y += velocidad;
  }

  void dibujar() {
    fill(255, 255, 0);
    rect(x, y, ancho, alto);
  }
}
