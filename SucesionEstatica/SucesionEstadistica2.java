import java.util.List;
import java.util.ArrayList;

//Otra posible implementación de la sucesión estadística, esta vez usando una lista en lugar de un arreglo. La ventaja de usar una lista es que no necesitamos preocuparnos por la capacidad máxima, ya que las listas pueden crecer dinámicamente. Sin embargo, en este caso, se ha mantenido la restricción de capacidad máxima para cumplir con los requisitos del ejercicio.
public class SucesionEstadistica2 {
    
    private List<Double> datos;
    private int capacidadMaxima; 

    public SucesionEstadistica2(int c) {
        if(c <= 0) {
            throw new IllegalArgumentException("Capacidad invalida");
        }
        this.capacidadMaxima = c;
        this.datos = new ArrayList<>(); //ArrayList implementa la interfaz List
    }

    public void agregarDato(double dato) {
        if (datos.size() < capacidadMaxima) {
            datos.add(dato);
        } else {
            throw new IllegalStateException("No se pueden agregar más datos, la sucesión está llena.");
        }
    }

    public int getCantidad() {
        return datos.size();
    }

}
