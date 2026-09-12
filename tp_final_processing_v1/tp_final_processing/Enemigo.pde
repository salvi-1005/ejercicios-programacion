abstract class Enemigo extends ElementoJuego {
  int vida;
  int puntosOtorgados;

  Enemigo(float x, float y, float ancho, float alto, float velocidad, int vida, int puntos) {
    super(x, y, ancho, alto, velocidad);
    this.vida = vida;
    this.puntosOtorgados = puntos;
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

  int getPuntosOtorgados() {
    return puntosOtorgados;
  }
}
