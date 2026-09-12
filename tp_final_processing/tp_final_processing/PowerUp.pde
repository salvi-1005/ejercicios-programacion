class PowerUp extends ElementoJuego {
  String tipo;

  PowerUp(float x, float y, String tipo) {
    super(x, y, 25, 25, 2);
    this.tipo = tipo;
  }

  void actualizar() {
    y += velocidad;
    if (y > height) desactivar();
  }

  void aplicarEfecto(Aermacchi jugador) {
    if (tipo.equals("vida")) {
      jugador.vida++;
    }
    desactivar();
  }

  void dibujar() {
    fill(0, 255, 120);
    ellipse(x, y, ancho, alto);
  }
}
