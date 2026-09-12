import java.util.ArrayList;

public class Libro {

    private ArrayList<Capitulo> capitulos;

    public Libro(int maxCapitulos) {
        this.capitulos = new ArrayList<>();
    }

    public void agregarCapitulo(Capitulo c) {
        capitulos.add(c);
    }

    // a)
    public ArrayList<String> getNombresCapitulos() {
        ArrayList<String> nombres = new ArrayList<>();
        for (Capitulo capitulo : capitulos) {
            nombres.add(capitulo.getNombre());
        }
        return nombres;
    }

    // b)
    public int getCantidadPaginasLibro() {
        int total = 0;
        for (Capitulo capitulo : capitulos) {
            total += capitulo.getCantidadPaginas();
        }
        return total;
    }

    public int getCantidadPaginasCapitulo(String nombre) {
        return buscarCapitulo(nombre).getCantidadPaginas();
    }

    // c)
    public int getPaginaInicialCapitulo(String nombre) {
        return buscarCapitulo(nombre).getPaginaInicial();
    }

    public int getPaginaFinalCapitulo(String nombre) {
        return buscarCapitulo(nombre).getPaginaFinal();
    }

    // d y e
    public int contarPalabrasLibro() {
        int total = 0;
        for (Capitulo capitulo : capitulos) {
            total += capitulo.contarPalabras();
        }
        return total;
    }

    public int contarCaracteresLibro() {
        int total = 0;
        for (Capitulo capitulo : capitulos) {
            total += capitulo.contarCaracteres();
        }
        return total;
    }

    // h)
    public String buscarContenidoPagina(int numero) {
        for (Capitulo capitulo : capitulos) {
            Pagina p = capitulo.buscarPagina(numero);
            if (p != null) {
                return p.getContenido();
            }
        }
        return null;
    }

    private Capitulo buscarCapitulo(String nombre) {
        for (Capitulo capitulo : capitulos) {
            if (capitulo.getNombre().equals(nombre)) {
                return capitulo;
            }
        }
        return null;
    }
}