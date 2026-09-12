abstract class Proyectil extends ElementoJuego {
  int danio;

  Proyectil(float x, float y, float velocidad, int danio) {
    super(x, y, 8, 16, velocidad);
    this.danio = danio;
  }

  int getDanio() {
    return danio;
  }

  boolean estaFueraDePantalla() {
    return y < -20 || y > height + 20;
  }
}
