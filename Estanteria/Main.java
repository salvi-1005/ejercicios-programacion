public class Main {

    public static void main(String[] args){
        Estante estante = new Estante();
        estante.agregarLibro(new Libro("El Quijote", "Miguel De Cervantes", "Editorial A", 1605));
        estante.agregarLibro(new Libro("Cien Años de Soledad", "Gabriel García Márquez", "Editorial B", 1967));
        estante.agregarLibro(new Libro("La Sombra del Viento", "Carlos Ruiz Zafón", "Editorial C", 2001));
        Estanteria estanteria = new Estanteria(1);
        estanteria.agregarEstante(estante, 0);
        estanteria.buscarLibro("Cien Años de Soledad");
        estanteria.listarLibrosEnUnEstanteEspecifico(0);
        estanteria.cambiarOrdenDeLosLibrosEnUnEstante(0);
        estanteria.listarLibrosEnUnEstanteEspecifico(0);
        System.out.println("Edad promedio de los libros en el estante 0: " + estanteria.calcularEdadPromedioDeLosLibrosEnUnEstante(0));
        System.out.println(estanteria.listarLibrosDeUnAutorEspecifico("Miguel De Cervantes"));
        System.out.println("Cantidad de libros en el estante 0: " + estante.getCantidadLibros());
    }
    
}
