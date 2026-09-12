public class Main {
    
    public static void main(String[] args) {
        Carta carta = new Carta("Corazones", "As");
        System.out.println("Carta: " + carta.getValor() + " de " + carta.getPalo());

        MazoPoker mazo = new MazoPoker();
        mazo.agregarCarta(new Carta("Corazones", "As"));

        mazo.barajarMazo();
        Carta cartaObtenida = mazo.getCarta(0);
        if (cartaObtenida != null) {
            System.out.println("Carta obtenida después de barajar: " + cartaObtenida.getValor() + " de " + cartaObtenida.getPalo());
        } else {
            System.out.println("No se pudo obtener una carta.");
        }

        mazo.sacarXCartasDeArriba(1);
        System.out.println("Cantidad de cartas después de sacar 1 carta de arriba: " + mazo.cantCartas());

        mazo.sacarXCartasDeAbajo(1);
        System.out.println("Cantidad de cartas después de sacar 1 carta de abajo: " + mazo.cantCartas());

        Carta[] nuevasCartas = {new Carta("Diamantes", "Rey"), new Carta("Picas", "Reina")};
        mazo.colocarXCartasArriba(nuevasCartas);
        System.out.println("Cantidad de cartas después de colocar 2 cartas en la parte superior: " + mazo.cantCartas());
        
        Carta[] nuevasCartas2 = {new Carta("Tréboles", "Diez"), new Carta("Corazones", "Nueve")};
        mazo.colocarXCartasAbajo(nuevasCartas2);
        System.out.println("Cantidad de cartas después de colocar 2 cartas en la parte inferior: " + mazo.cantCartas());
    }


}
