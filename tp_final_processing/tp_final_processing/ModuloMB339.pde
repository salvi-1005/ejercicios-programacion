class ModuloMB339 {
  Aermacchi jugador;
  ArrayList<ElementoJuego> elementos;
  GestorColisiones gestorColisiones;
  EstadisticasModulo estadisticas;
  EstadisticasGenerales estadisticasGenerales;
  boolean pausado;
  boolean finalizado;

  boolean izquierda, derecha, arriba, abajo, disparo;

  ModuloMB339() {
    elementos = new ArrayList<ElementoJuego>();
    gestorColisiones = new GestorColisiones();
    estadisticas = new EstadisticasModulo();
    estadisticasGenerales = new EstadisticasGenerales();
  }

  void inicializar() {
    jugador = new Aermacchi(width / 2, height - 100);
    elementos.add(jugador);
    estadisticas.reiniciarEstadisticas();
  }

  void iniciar() {
    pausado = false;
    finalizado = false;
  }

  void actualizarCiclo() {
    if (pausado || finalizado) return;

    moverJugador();

    if (disparo) {
      dispararJugador();
    }

    generarEnemigos();
    actualizarElementos();
    gestorColisiones.verificarColisiones(elementos, estadisticas);
    eliminarElementosInactivos();
    verificarFinPartida();
  }

  void moverJugador() {
    if (izquierda) jugador.mover("izquierda");
    if (derecha) jugador.mover("derecha");
    if (arriba) jugador.mover("arriba");
    if (abajo) jugador.mover("abajo");
  }

  void dispararJugador() {
    if (jugador.puedeDisparar()) {
      ProyectilAliado p = jugador.disparar();
      elementos.add(p);
      estadisticas.registrarDisparo(false);
    }
  }

  void generarEnemigos() {
    if (frameCount % 80 == 0) {
      elementos.add(new CazaEnemigo(random(40, width - 40), -40));
    }

    if (frameCount % 240 == 0) {
      elementos.add(new BateriaEnemiga(random(50, width - 50), -40));
    }
  }

  void actualizarElementos() {
  for (int i = 0; i < elementos.size(); i++) {
    ElementoJuego e = elementos.get(i);
    e.actualizar();
    }
  }

  void eliminarElementosInactivos() {
    for (int i = elementos.size() - 1; i >= 0; i--) {
      if (!elementos.get(i).estaActivo()) {
        elementos.remove(i);
      }
    }
  }

  void verificarFinPartida() {
    if (jugador.estaDestruido()) {
      finalizado = true;
      estadisticasGenerales.registrarDerrota();
    }

    if (estadisticas.puntajeTotal >= 10000 || estadisticas.enemigosDerribados >= 100) {
      finalizado = true;
      estadisticasGenerales.registrarVictoria();
    }
  }

  void dibujar() {
    for (ElementoJuego e : elementos) {
      e.dibujar();
    }

    dibujarHUD();

    if (pausado) {
      textAlign(CENTER);
      textSize(40);
      fill(255);
      text("PAUSA", width / 2, height / 2);
    }

    if (finalizado) {
      textAlign(CENTER);
      textSize(35);
      fill(255, 80, 80);
      text("FIN DEL JUEGO", width / 2, height / 2);
    }
  }

  void dibujarHUD() {
    fill(255);
    textAlign(LEFT);
    textSize(16);
    text("Vidas: " + jugador.vida, 20, 25);
    text("Puntaje: " + estadisticas.puntajeTotal, 20, 50);
    text("Enemigos derribados: " + estadisticas.enemigosDerribados, 20, 75);
    text("Precisión: " + nf((float)estadisticas.calcularPrecision(), 1, 2) + "%", 20, 100);
  }

  void teclaPresionada(int code, char tecla) {
    if (code == LEFT || tecla == 'a' || tecla == 'A') izquierda = true;
    if (code == RIGHT || tecla == 'd' || tecla == 'D') derecha = true;
    if (code == UP || tecla == 'w' || tecla == 'W') arriba = true;
    if (code == DOWN || tecla == 's' || tecla == 'S') abajo = true;
    if (tecla == ' ') disparo = true;

    if (tecla == 'p' || tecla == 'P') {
      pausado = !pausado;
    }
  }

  void teclaSoltada(int code, char tecla) {
    if (code == LEFT || tecla == 'a' || tecla == 'A') izquierda = false;
    if (code == RIGHT || tecla == 'd' || tecla == 'D') derecha = false;
    if (code == UP || tecla == 'w' || tecla == 'W') arriba = false;
    if (code == DOWN || tecla == 's' || tecla == 'S') abajo = false;
    if (tecla == ' ') disparo = false;
  }
  
}
