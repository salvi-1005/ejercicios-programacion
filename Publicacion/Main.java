public class Main {
    public static void main(String[] args) {

        Libro libro = new Libro("El Quijote", 5000, 800, 1605);
        Disco disco = new Disco("Greatest Hits", 3000, 60);

        System.out.println("=== LIBRO ===");
        libro.mostrarDatos();

        System.out.println("\n=== DISCO ===");
        disco.mostrarDatos();
    }
}
