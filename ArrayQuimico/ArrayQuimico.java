import java.util.ArrayList;
import java.util.Collections;

public class ArrayQuimico {

    private ArrayList<ComponenteQuimico> datos;

    public ArrayQuimico() {
        this.datos = new ArrayList<>();
    }

    public void agregar(ComponenteQuimico c) {
        datos.add(c);
    }

    public ArrayList<ComponenteQuimico> getDatos() {
        return datos;
    }

    public void ordenar() {
        Collections.sort(datos);
    }

    public void ordenarConComparator() {
        Collections.sort(datos, new ComparadorQuimico());
    }
    
}
