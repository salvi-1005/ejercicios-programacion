public class Venta extends Reporte implements Imprimible, Customizable{
    
    private String colorFondo;
    private String colorLetra;

    public Venta(String titulo, String contenido, String colorFondo, String colorLetra){
        super(titulo, contenido);
        this.colorFondo = colorFondo;
        this.colorLetra = colorLetra;
    }

    @Override
    public void imprimir(){
        System.out.println("Título: " + getTitulo());
        System.out.println("Contenido: " + getContenido());
        System.out.println("Color de fondo: " + colorFondo);
        System.out.println("Color de letra: " + colorLetra);
    }

    public void customizar(String colorFondo, String colorLetra){
        this.colorFondo = colorFondo;
        this.colorLetra = colorLetra;
    }
    
}
