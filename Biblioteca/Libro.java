public class Libro {

    private String titulo;
    private Autor autor;
    private int año;
    private int cantPaginas;

    public Libro(String titulo, Autor autor, int año, int cantPaginas){
        this.titulo = titulo;
        this.autor = autor;
        this.año = año;
        this.cantPaginas = cantPaginas;
    }

    public String getTitulo(){
        return this.titulo;
    }

    public void setTitulo(String nuevoTitulo){
        this.titulo = nuevoTitulo;
    }

    public Autor getAutor(){
        return this.autor;
    }

    public void setAutor(Autor nuevoAutor){
        this.autor = nuevoAutor;
    }

    public int getAño(){
        return this.año;
    }

    public void setAño(int nuevoAño){
        this.año = nuevoAño;
    }

    public int getCantPaginas(){
        return this.cantPaginas;
    }

    public void setCantPaginas(int nuevoPaginas){
        this.cantPaginas = nuevoPaginas;
    }

    public String toString(){
        return ("- Titulo: " + titulo + " - Autor: " + autor + " - Año: " + año + " - Cantidad de paginas: " + cantPaginas);
    }

}
