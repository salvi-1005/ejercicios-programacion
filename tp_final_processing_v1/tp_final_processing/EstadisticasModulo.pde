class EstadisticasModulo {
  int disparosTotales = 0;
  int disparosAcertados = 0;
  int rachaMaxDerribos = 0;
  int rachaActual = 0;
  int enemigosDerribados = 0;
  int puntajeTotal = 0;
  double precision = 0;

  void registrarDisparo(boolean acerto) {
    disparosTotales++;

    if (acerto) {
      disparosAcertados++;
    }

    calcularPrecision();
  }

  void registrarImpacto() {
    disparosAcertados++;
    calcularPrecision();
  }

  void registrarDerribo(int puntos) {
    enemigosDerribados++;
    puntajeTotal += puntos;
    rachaActual++;

    if (rachaActual > rachaMaxDerribos) {
      rachaMaxDerribos = rachaActual;
    }

    calcularPrecision();
  }

  void registrarMuerteJugador() {
    rachaActual = 0;
  }

  double calcularPrecision() {
    if (disparosTotales == 0) {
      precision = 0;
    } else {
      precision = (disparosAcertados * 100.0) / disparosTotales;
    }

    return precision;
  }

  void reiniciarEstadisticas() {
    disparosTotales = 0;
    disparosAcertados = 0;
    rachaMaxDerribos = 0;
    rachaActual = 0;
    enemigosDerribados = 0;
    puntajeTotal = 0;
    precision = 0;
  }
}
