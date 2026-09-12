public class Compra extends Reporte implements Imprimible {
    
    public Compra(String tit, String cont){
        super(tit, cont);
        
    }
    
    @Override
    public void imprimir(){
        System.out.println("Título: " + getTitulo());
        System.out.println("Contenido: " + getContenido());
    }
}
