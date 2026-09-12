import java.util.ArrayList;

public class Usuario {

    private String nombre;
    private ArrayList<Contenido> historial; 
    public Usuario(String nombre){
        this.nombre = nombre;
        this.historial = new ArrayList<>();
    }

    public String getNombre(){
        return this.nombre;
    }

    public ArrayList<Contenido> getHistorial(){
        return this.historial;
    }

    public void verContenido(Contenido c){
        historial.add(c);
        c.registrarVisualizacion(new Visualizacion(this.nombre));
    }
    
}
