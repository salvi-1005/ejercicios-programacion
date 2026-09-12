import java.time.LocalDate;

public class Main {

    public static void main(String[] args){

        Biblioteca biblioteca = new Biblioteca("Ananda");

        Libro libro1 = biblioteca.agregarLibro(new Libro("El Gigante Egoista", new Autor("Oscar", "Wilde", LocalDate.of(1854, 10, 16)), 1888, 50));
        Libro libro2 = biblioteca.agregarLibro(new Libro("Pajaros En La Boca", new Autor("Samanta", "Schweblin", LocalDate.of(1978, 5, 10)), 2008, 70));
        Libro libro3 = biblioteca.agregarLibro(new Libro("El Pan De La Locura", new Autor("Carlos", "Gorostiza", LocalDate.of(1920, 6, 7)), 1958, 100));

        biblioteca.mostrarLibrosDeUnAutor(libro1.getAutor());
        biblioteca.mostrarLibrosDeUnAutor(libro2.getAutor());
        biblioteca.mostrarLibrosDeUnAutor(libro3.getAutor());

        biblioteca.mostrarLibrosPublicadosDespuesDeCiertoAño(1900);

        biblioteca.mostrarElLibroConMasPaginas();

        biblioteca.ordenarLibrosPorAño();

    }
    
}
