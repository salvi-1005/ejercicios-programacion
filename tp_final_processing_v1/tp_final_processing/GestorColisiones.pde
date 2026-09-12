class GestorColisiones {
  void verificarColisiones(ArrayList<ElementoJuego> elementos, EstadisticasModulo stats) {
    for (int i = 0; i < elementos.size(); i++) {
      ElementoJuego a = elementos.get(i);

      for (int j = i + 1; j < elementos.size(); j++) {
        ElementoJuego b = elementos.get(j);

        if (a.estaActivo() && b.estaActivo() && verificarColision(a, b)) {
          procesarColision(a, b, stats);
        }
      }
    }
  }

  boolean verificarColision(ElementoJuego a, ElementoJuego b) {
    return a.getHitbox().intersecta(b.getHitbox());
  }

  void procesarColision(ElementoJuego a, ElementoJuego b, EstadisticasModulo stats) {
    if (a instanceof ProyectilAliado && b instanceof Enemigo) {
      impactoProyectilEnemigo((ProyectilAliado)a, (Enemigo)b, stats);
    } else if (b instanceof ProyectilAliado && a instanceof Enemigo) {
      impactoProyectilEnemigo((ProyectilAliado)b, (Enemigo)a, stats);
    }

    if (a instanceof ProyectilEnemigo && b instanceof Aermacchi) {
      impactoJugador((ProyectilEnemigo)a, (Aermacchi)b, stats);
    } else if (b instanceof ProyectilEnemigo && a instanceof Aermacchi) {
      impactoJugador((ProyectilEnemigo)b, (Aermacchi)a, stats);
    }

    if (a instanceof Aermacchi && b instanceof Enemigo) {
      choqueJugadorEnemigo((Aermacchi)a, (Enemigo)b, stats);
    } else if (b instanceof Aermacchi && a instanceof Enemigo) {
      choqueJugadorEnemigo((Aermacchi)b, (Enemigo)a, stats);
    }

    if (a instanceof Aermacchi && b instanceof PowerUp) {
      ((PowerUp)b).aplicarEfecto((Aermacchi)a);
    } else if (b instanceof Aermacchi && a instanceof PowerUp) {
      ((PowerUp)a).aplicarEfecto((Aermacchi)b);
    }
  }

  void impactoProyectilEnemigo(ProyectilAliado p, Enemigo e, EstadisticasModulo stats) {
    e.recibirImpacto(p.getDanio());
    p.desactivar();

    stats.registrarImpacto();

    if (e.estaDestruido()) {
      stats.registrarDerribo(e.getPuntosOtorgados());
    }
  }

  void impactoJugador(ProyectilEnemigo p, Aermacchi jugador, EstadisticasModulo stats) {
    jugador.recibirImpacto(p.getDanio());
    p.desactivar();

    if (jugador.estaDestruido()) {
      stats.registrarMuerteJugador();
    }
  }

  void choqueJugadorEnemigo(Aermacchi jugador, Enemigo enemigo, EstadisticasModulo stats) {
    jugador.recibirImpacto(1);
    enemigo.desactivar();

    if (jugador.estaDestruido()) {
      stats.registrarMuerteJugador();
    }
  }
}
