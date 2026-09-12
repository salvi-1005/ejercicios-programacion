public class Publicacion {

    protected String titulo;
    protected double precio;
    
    public Publicacion(String titulo, double precio){
        this.titulo = titulo;
        this.precio = precio;
    }

    public String getTitulo(){
        return titulo;
    }

    public double getPrecio(){
        return precio;
    }

    public void mostrarDatos() {
        System.out.println("Titulo: " + titulo + ", Precio: " + precio);
    }
}
