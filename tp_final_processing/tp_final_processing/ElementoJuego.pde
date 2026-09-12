abstract class ElementoJuego {
  float x, y;
  float ancho, alto;
  float velocidad;
  boolean activo = true;

  ElementoJuego(float x, float y, float ancho, float alto, float velocidad) {
    this.x = x;
    this.y = y;
    this.ancho = ancho;
    this.alto = alto;
    this.velocidad = velocidad;
  }

  abstract void actualizar();
  abstract void dibujar();

  Rectangle getHitbox() {
    return new Rectangle(x, y, ancho, alto);
  }

  boolean estaActivo() {
    return activo;
  }

  void desactivar() {
    activo = false;
  }
}
