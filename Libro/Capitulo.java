public class Capitulo {

    private String nombre;
    private Pagina[] paginas;
    private int cantPaginas;

    public Capitulo(String nombre, int maxPaginas) {
        this.nombre = nombre;
        this.paginas = new Pagina[maxPaginas];
        this.cantPaginas = 0;
    }

    public String getNombre() {
        return nombre;
    }

    // g) agregar página
    public void agregarPagina(Pagina p) {
        paginas[cantPaginas] = p;
        cantPaginas++;
    }

    // g) eliminar página
    public void eliminarPagina(int numero) {
        for (int i = 0; i < cantPaginas; i++) {
            if (paginas[i].getNumero() == numero) {
                for (int j = i; j < cantPaginas - 1; j++) {
                    paginas[j] = paginas[j + 1];
                }
                cantPaginas--;
                break;
            }
        }
    }

    // b)
    public int getCantidadPaginas() {
        return cantPaginas;
    }

    // c)
    public int getPaginaInicial() {
        return paginas[0].getNumero();
    }

    public int getPaginaFinal() {
        return paginas[cantPaginas - 1].getNumero();
    }

    // d y e
    public int contarPalabras() {
        int total = 0;
        for (int i = 0; i < cantPaginas; i++) {
            total += paginas[i].contarPalabras();
        }
        return total;
    }

    public int contarCaracteres() {
        int total = 0;
        for (int i = 0; i < cantPaginas; i++) {
            total += paginas[i].contarCaracteres();
        }
        return total;
    }

    // h)
    public Pagina buscarPagina(int numero) {
        for (int i = 0; i < cantPaginas; i++) {
            if (paginas[i].getNumero() == numero) {
                return paginas[i];
            }
        }
        return null;
    }
}
