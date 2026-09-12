import java.util.Arrays;

public class Mazo {
    
    private Carta[] cartas;
    private int cantCartas;
    private int indice;

    public Mazo() {
        this.cartas = new Carta[52];
        this.cantCartas = 52;
        this.indice = 52;
    }

    public void agregarCarta(Carta c) {
        cartas[cantCartas] = c;
        cantCartas++;
    }

    public Carta getCarta(int indice) {
        if (indice >= 0 && indice < cantCartas) {
            return cartas[indice];
        }
        return null; // o lanzar una excepción
    }

    
    public Carta robarCarta() {
        if (indice == 0) {
            System.out.println("No quedan cartas");
            return null;
        }
        return cartas[--indice];
    }

    public void barajarMazo() {
        for (int i = 0; i < cantCartas; i++) {
            int j = (int) (Math.random() * cantCartas);
            Carta temp = cartas[i];
            cartas[i] = cartas[j];
            cartas[j] = temp;
        }
    }

    public void sacarXCartasDeArriba(int x) {
        if (x <= cantCartas) {
            for (int i = 0; i < x; i++) {
                cartas[i] = null; // o mover las cartas restantes hacia arriba
            }
            // Si se desea mover las cartas restantes hacia arriba:
            for (int i = x; i < cantCartas; i++) {
                cartas[i - x] = cartas[i];
                cartas[i] = null;
            }
            cantCartas -= x;
        }
    }

    public void sacarXCartasDeAbajo(int x) {
        if (x <= cantCartas) {
            for (int i = cantCartas - x; i < cantCartas; i++) {
                cartas[i] = null; // o mover las cartas restantes hacia abajo
            }
            // Si se desea mover las cartas restantes hacia abajo:
            for (int i = cantCartas - x - 1; i >= 0; i--) {
                cartas[i + x] = cartas[i];
                cartas[i] = null;
            }
            cantCartas -= x;
        }
    }

    public void colocarXCartasArriba(Carta[] nuevasCartas) {
        if (cantCartas + nuevasCartas.length > cartas.length) {
            System.out.println("No hay espacio en el mazo");
        return;
        }
        // 1. Mover las cartas existentes hacia abajo
        for (int j = cantCartas - 1; j >= 0; j--) {
            cartas[j + nuevasCartas.length] = cartas[j];
        }
        // 2. Insertar las nuevas cartas arriba
        for (int i = 0; i < nuevasCartas.length; i++) {
            cartas[i] = nuevasCartas[i];
        }
        // 3. Actualizar cantidad
        cantCartas += nuevasCartas.length;
    }


    public void colocarXCartasAbajo(Carta[] nuevasCartas) {
        
        if (cantCartas >= cartas.length){
            System.out.println("No hay espacio en el mazo");
            return;
        }
        for (int i = 0; i < nuevasCartas.length; i++) { 
            cartas[cantCartas] = nuevasCartas[i];
            cantCartas++;
        }
    }

    public void ordenarPorPalo() {
        Arrays.sort(cartas, (c1, c2) -> Integer.compare(valorPalo(c1.getPalo()),valorPalo(c2.getPalo())));
    }

    
    private int valorPalo(String palo){
        switch(palo){
            case "Picas": return 1;
            case "Corazones": return 2;
            case "Diamantes": return 3;
            case "Treboles": return 4;
            default: return 0;
        }
    }


    public int cantCartas() {
        return cantCartas;
    }

}
