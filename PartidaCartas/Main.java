public class Main {

    public static void main(String[] args) {
        Jugador jugador1 = new Jugador("Jugador 1");
        Jugador jugador2 = new Jugador("Jugador 2");

        // Agregar cartas a los jugadores (ejemplo)
        jugador1.agregarCarta(new Carta("Corazones", "1"));
        jugador1.agregarCarta(new Carta("Diamantes", "2"));
        jugador1.agregarCarta(new Carta("Tréboles", "3"));
        jugador1.agregarCarta(new Carta("Picas", "4"));
        jugador1.agregarCarta(new Carta("Corazones", "5"));

        jugador2.agregarCarta(new Carta("Corazones", "5"));
        jugador2.agregarCarta(new Carta("Diamantes", "6"));
        jugador2.agregarCarta(new Carta("Tréboles", "7"));
        jugador2.agregarCarta(new Carta("Picas", "8"));
        jugador2.agregarCarta(new Carta("Corazones", "9"));

        System.out.println(jugador1.getNombre() + " tiene " + jugador1.getPuntos() + " puntos.");
        System.out.println(jugador2.getNombre() + " tiene " + jugador2.getPuntos() + " puntos.");

        PartidaCartas partida = new PartidaCartas(jugador1, jugador2);
        partida.jugarMultiplesRondas(10);
        Jugador ganador = partida.quienGana();
        if (ganador != null) {
            System.out.println(ganador.getNombre() + " gana la partida.");
        } else {
            System.out.println("La partida termina en empate.");
        }

        Jugador jugadorConCartaMasAlta = partida.quienTieneLaCartaMasAlta();
        System.out.println("El jugador con la carta más alta es: " + (jugadorConCartaMasAlta != null ? jugadorConCartaMasAlta.getNombre() : "Empate"));

        Jugador jugadorConNumeroMasAlto = partida.quienTieneElNumeroDeDosDigitosMasAltoQueSePuedeFormarConCartasDel1al9sinContarJQyK();
        System.out.println("El jugador con el número de dos dígitos más alto es: " + (jugadorConNumeroMasAlto != null ? jugadorConNumeroMasAlto.getNombre() : "Empate"));


    }
    
}
