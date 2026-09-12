import java.util.ArrayList;
import java.util.Comparator;

public class Biblioteca {

    public String nombre;
    public ArrayList<Libro> libros;
    
    public Biblioteca(String nombre){
        this.nombre = nombre;
        this.libros = new ArrayList<>();
    }

    public Libro agregarLibro(Libro libro){
        libros.add(libro);
        return libro;
    }

    public void mostrarLibrosDeUnAutor(Autor autor){
        System.out.println("Libros de " + autor.getNombre() + " " + autor.getApellido() + ":");
        for (Libro libro : libros){
            if (libro.getAutor().equals(autor)){
                System.out.println(libro.toString());

            }
        }
    }

    public void mostrarLibrosPublicadosDespuesDeCiertoAño(int año){
        System.out.println("Libros publicados despues de: " + año);
        for (Libro libro : libros){
            if (libro.getAño() >= año){
                System.out.println(libro.toString());

            }
        }
    }

    public void mostrarElLibroConMasPaginas(){
        System.out.println("El libro con mas paginas es: ");
        Libro libroConMasPaginas = null;
        for (Libro libro : libros){
            if (libroConMasPaginas == null || libro.getCantPaginas() > libroConMasPaginas.getCantPaginas()){
                libroConMasPaginas = libro;
            }
        }
        if (libroConMasPaginas != null){
            System.out.println(libroConMasPaginas.toString());
        } else{
            System.out.println("No hay libros en la biblioteca");
        }
    }

    public void ordenarLibrosPorAño(){
        System.out.println("Libros ordenados por año: ");
        libros.sort(Comparator.comparingInt(Libro::getAño));
        for (Libro libro : libros) {
            System.out.println(libro.toString());
        }
    }
    
}
