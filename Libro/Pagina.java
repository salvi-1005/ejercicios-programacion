public class Pagina {

    private int numero;
    private String contenido;
    private Referencia[] referencias;
    private int cantReferencias;

    public Pagina(int numero, String contenido) {
        this.numero = numero;
        this.contenido = contenido;
        this.referencias = new Referencia[10]; // fijo, simple
        this.cantReferencias = 0;
    }

    public int getNumero() {
        return numero;
    }

    public String getContenido() {
        return contenido;
    }

    public int contarPalabras() {
        return contenido.split(" ").length;
    }

    public int contarCaracteres() {
        return contenido.length();
    }

    // f) agregar referencia
    public void agregarReferencia(String texto) {
        referencias[cantReferencias] = new Referencia(texto);
        cantReferencias++;
    }
}
