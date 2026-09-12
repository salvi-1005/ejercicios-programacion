public class PartidaCartas{

    private Jugador jugador1;
    private Jugador jugador2;
    private Mazo mazo;

    public PartidaCartas(Jugador jugador1, Jugador jugador2) {
        this.jugador1 = jugador1;
        this.jugador2 = jugador2;
        mazo = new Mazo();
    }

    public Jugador quienGana() {
        if (jugador1.getPuntos() > jugador2.getPuntos()) {
            return jugador1;
        } else if (jugador2.getPuntos() > jugador1.getPuntos()) {
            return jugador2;
        } else {
            return null; // Empate
        }
    }

    public void repartirCartas() {
        jugador1.vaciarMano();
        jugador2.vaciarMano();
        // repartir 5 cartas a cada uno
        for (int i = 0; i < 5; i++) {
            jugador1.agregarCarta(mazo.robarCarta());
            jugador2.agregarCarta(mazo.robarCarta());
        }
    }

    public void jugarMultiplesRondas(int cantRondas) {
        int victoriasJugador1 = 0;
        int victoriasJugador2 = 0;
        for (int i = 0; i < cantRondas; i++) {

            mazo = new Mazo();
            mazo.barajarMazo();
            repartirCartas();

            if (jugador1.getPuntos() > jugador2.getPuntos()) {
                victoriasJugador1++;
            } else if (jugador2.getPuntos() > jugador1.getPuntos()) {
                victoriasJugador2++;
            }
        }
        if (victoriasJugador1 > victoriasJugador2) {
            System.out.println(jugador1.getNombre() + " gana la partida con " + victoriasJugador1 + " victorias.");
        } else if (victoriasJugador2 > victoriasJugador1) {
            System.out.println(jugador2.getNombre() + " gana la partida con " + victoriasJugador2 + " victorias.");
        } else {
            System.out.println("La partida termina en empate con " + victoriasJugador1 + " victorias para cada jugador.");
        }
    }

    public Jugador quienTieneLaCartaMasAlta() {
        Carta cartaMasAltaJugador1 = null;
        Carta cartaMasAltaJugador2 = null;
        Carta[] manoJugador1 = new Carta[5];
        Carta[] manoJugador2 = new Carta[5];
        for (int i = 0; i < jugador1.getMano().length; i++) {
            if (jugador1.getMano()[i] != null && (jugador1.getMano()[i].getValor().equals("1") || jugador1.getMano()[i].getValor().equals("2") || jugador1.getMano()[i].getValor().equals("3") || jugador1.getMano()[i].getValor().equals("4") || jugador1.getMano()[i].getValor().equals("5") || jugador1.getMano()[i].getValor().equals("6") || jugador1.getMano()[i].getValor().equals("7") || jugador1.getMano()[i].getValor().equals("8") || jugador1.getMano()[i].getValor().equals("9") || jugador1.getMano()[i].getValor().equals("10"))) {
                manoJugador1[i] = jugador1.getMano()[i];
            }
            if (jugador1.getMano()[i] != null && (jugador1.getMano()[i].getValor().equals("J") )) {
                manoJugador1[i] = new Carta(jugador1.getMano()[i].getPalo(), "11");
            }
            if (jugador1.getMano()[i] != null && (jugador1.getMano()[i].getValor().equals("Q") )) {
                manoJugador1[i] = new Carta(jugador1.getMano()[i].getPalo(), "12");
            }
            if (jugador1.getMano()[i] != null && (jugador1.getMano()[i].getValor().equals("K") )) {
                manoJugador1[i] = new Carta(jugador1.getMano()[i].getPalo(), "13");
            }
        }
        for (int i = 0; i < jugador2.getMano().length; i++) {
            if (jugador2.getMano()[i] != null && (jugador2.getMano()[i].getValor().equals("1") || jugador2.getMano()[i].getValor().equals("2") || jugador2.getMano()[i].getValor().equals("3") || jugador2.getMano()[i].getValor().equals("4") || jugador2.getMano()[i].getValor().equals("5") || jugador2.getMano()[i].getValor().equals("6") || jugador2.getMano()[i].getValor().equals("7") || jugador2.getMano()[i].getValor().equals("8") || jugador2.getMano()[i].getValor().equals("9") || jugador2.getMano()[i].getValor().equals("10"))) {
                manoJugador2[i] = jugador2.getMano()[i];
            }
            if (jugador2.getMano()[i] != null && (jugador2.getMano()[i].getValor().equals("J"))) {
                manoJugador2[i] = new Carta(jugador2.getMano()[i].getPalo(), "11");
            }
            if (jugador2.getMano()[i] != null && (jugador2.getMano()[i].getValor().equals("Q") )) {
                manoJugador2[i] = new Carta(jugador2.getMano()[i].getPalo(), "12");
            }
            if (jugador2.getMano()[i] != null && (jugador2.getMano()[i].getValor().equals("K") )) {
                manoJugador2[i] = new Carta(jugador2.getMano()[i].getPalo(), "13");
            }
        }
        for (Carta carta : manoJugador1) {
            if (carta != null) {
                if (cartaMasAltaJugador1 == null || Integer.parseInt(carta.getValor()) > Integer.parseInt(cartaMasAltaJugador1.getValor())) {
                    cartaMasAltaJugador1 = carta;
                }
            }
        }
        for (Carta carta : manoJugador2) {
            if (carta != null) {
                if (cartaMasAltaJugador2 == null || Integer.parseInt(carta.getValor()) > Integer.parseInt(cartaMasAltaJugador2.getValor())) {
                    cartaMasAltaJugador2 = carta;
                }
            }
        }
        if (Integer.parseInt(cartaMasAltaJugador1.getValor()) > Integer.parseInt(cartaMasAltaJugador2.getValor())) {
            return jugador1;
        } else if (Integer.parseInt(cartaMasAltaJugador2.getValor()) > Integer.parseInt(cartaMasAltaJugador1.getValor())) {
            return jugador2;
        } else {
            return null; // Empate
        }
    }

    public Jugador quienTieneMasCartasConElMismoValor() {
        int cartasJugador1 = 0;
        int cartasJugador2 = 0;
        for (Carta carta : jugador1.getMano()) {
            if (carta != null) {
                for (Carta carta2 : jugador1.getMano()) {
                    if (carta2 != null && carta.getValor().equals(carta2.getValor())) {
                        cartasJugador1++;
                    }
                }
            }
        }
        for (Carta carta : jugador2.getMano()) {
            if (carta != null) {
                for (Carta carta2 : jugador2.getMano()) {
                    if (carta2 != null && carta.getValor().equals(carta2.getValor())) {
                        cartasJugador2++;
                    }
                }
            }
        }
        if (cartasJugador1 > cartasJugador2) {
            return jugador1;
        } else if (cartasJugador2 > cartasJugador1) {
            return jugador2;
        } else {
            return quienTieneLaCartaMasAlta(); // Si hay empate en el número de cartas con el mismo valor, se desempata con la carta más alta
        }
    }

    public Jugador quienTieneElNumeroDeDosDigitosMasAltoQueSePuedeFormarConCartasDel1al9sinContarJQyK() {
        int numeroJugador1 = jugador1.cualEsElNumeroDeDosDigitosMasAltoQueSePuedeFormarConCartasDel1al9sinContarJQyK();
        int numeroJugador2 = jugador2.cualEsElNumeroDeDosDigitosMasAltoQueSePuedeFormarConCartasDel1al9sinContarJQyK();
        if (numeroJugador1 > numeroJugador2) {
            return jugador1;
        } else if (numeroJugador2 > numeroJugador1) {
            return jugador2;
        } else {
            return null; // Empate
        }
    }

}