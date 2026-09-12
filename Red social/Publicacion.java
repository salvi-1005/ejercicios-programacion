public class Publicacion {
    
    private String titulo;
    private String contenido;
    private Usuario autor;
    private int cantidadDeLikes;

    public Publicacion(String titulo, String contenido, Usuario autor) {
        this.titulo = titulo;
        this.contenido = contenido;
        this.autor = autor;
        this.cantidadDeLikes = 0;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getContenido() {
        return contenido;
    }

    public void setContenido(String contenido) {
        this.contenido = contenido;
    }

    public Usuario getAutor() {
        return autor;
    }

    public void setAutor(Usuario autor) {
        this.autor = autor;
    }

    public int getCantidadDeLikes() {
        return cantidadDeLikes;
    }

    public void setCantidadDeLikes(int cantidadDeLikes) {
        this.cantidadDeLikes = cantidadDeLikes;
    }

}
