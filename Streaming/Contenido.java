import java.util.ArrayList;

public abstract class Contenido {

    protected String nombre;
    protected ArrayList<Visualizacion> visualizaciones;
    protected int cantVisualizaciones;

    public Contenido(String nombre){
        this.nombre = nombre;
        this.visualizaciones = new ArrayList<>();
        cantVisualizaciones = 0;
    }

    public String getNombre(){
        return this.nombre;
    }

    public Visualizacion registrarVisualizacion(Visualizacion visualizacion){
        visualizaciones.add(visualizacion);
        cantVisualizaciones += 1;
        return visualizacion;
    }

    public int getCantidadVisualizaciones(){
        return cantVisualizaciones;
    }

    
}
