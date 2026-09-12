public class Libro{

    private String nombre;
    private String autor;
    private String editorial;
    private int añoPublicacion;

    public Libro(String nombre, String autor, String editorial, int añoPublicacion) {
        this.nombre = nombre;
        this.autor = autor;
        this.editorial = editorial;
        this.añoPublicacion = añoPublicacion;
    }

    public String getNombre() {
        return nombre;
    }

    public String getAutor() {
        return autor;
    }

    public String getEditorial() {
        return editorial;
    }

    public int getAñoPublicacion() {
        return añoPublicacion;
    }

}