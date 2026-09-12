public abstract class Reporte {
    
    protected String titulo;
    protected String contenido;

    public Reporte(String titulo, String contenido){
        this.titulo = titulo;
        this.contenido = contenido;
    }

    public String getTitulo(){
        return titulo;
    }

    public String getContenido(){
        return contenido;
    }

    public abstract void imprimir();

}
