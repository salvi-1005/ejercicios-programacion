class EstadisticasGenerales {
  int puntajeTotal = 0;
  int partidasJugadas = 0;
  int partidasGanadas = 0;
  int partidasPerdidas = 0;
  int enemigosDestruidos = 0;
  long tiempoJugadoSegundos = 0;

  void registrarVictoria() {
    partidasJugadas++;
    partidasGanadas++;
  }

  void registrarDerrota() {
    partidasJugadas++;
    partidasPerdidas++;
  }

  void agregarPuntos(int puntos) {
    puntajeTotal += puntos;
  }

  void registrarEnemigosDestruidos(int cantidad) {
    enemigosDestruidos += cantidad;
  }

  void sumarTiempo(long segundos) {
    tiempoJugadoSegundos += segundos;
  }

  double calcularPorcentajeVictorias() {
    if (partidasJugadas == 0) {
      return 0;
    }

    return (partidasGanadas * 100.0) / partidasJugadas;
  }

  void finalizarEstadistica() {
  }

  void reiniciarEstadisticas() {
    puntajeTotal = 0;
    partidasJugadas = 0;
    partidasGanadas = 0;
    partidasPerdidas = 0;
    enemigosDestruidos = 0;
    tiempoJugadoSegundos = 0;
  }
}
