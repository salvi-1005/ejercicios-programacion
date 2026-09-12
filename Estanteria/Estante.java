public class Estante {
    
    private Libro[] libros;
    private int cantidadLibros;

    public Estante() {
        this.cantidadLibros = 0;
        this.libros = new Libro[10];
    }

    public Libro[] getLibros() {
        return libros;
    }

    public int getCantidadLibros() {
        return cantidadLibros;
    }

    public void agregarLibro(Libro libro) {
        if (cantidadLibros < libros.length) {
            libros[cantidadLibros] = libro;
            cantidadLibros++;
        } else {
            System.out.println("No se pueden agregar más libros, el estante está lleno.");
        }
    }

    public void eliminarLibro(int posicion) {
        if (posicion < cantidadLibros) {
            for (int i = posicion; i < cantidadLibros - 1; i++) {
                libros[i] = libros[i + 1];
            }
            libros[cantidadLibros - 1] = null;
            cantidadLibros--;
        } else {
            System.out.println("No se puede eliminar el libro, posición inválida.");
        }
    }


}
