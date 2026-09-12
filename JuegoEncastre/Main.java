public class Main {
    
    public static void main(String[] args) {
        Hueco[] huecos = {
            new Hueco(5, 5, 5),
            new Hueco(10, 10, 10),
            new Hueco(15, 15, 15)
        };

        Bloque[] bloques = {
            new Bloque(5, 5, 5),
            new Bloque(10, 10, 10),
            new Bloque(15, 15, 15)
        };

        JuegoEncastre juego = new JuegoEncastre(huecos, bloques);
        int intentos = juego.intentosNecesarios();
        System.out.println("Número de intentos necesarios: " + intentos);
    }

}
