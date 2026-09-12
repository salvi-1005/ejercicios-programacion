import java.util.ArrayList;
import java.util.Collections;

public class MiArrayList<T extends Comparable<T>> {

    private ArrayList<T> datos;

    public MiArrayList() {
        this.datos = new ArrayList<>();
    }

    public void agregar(T elem) {
        datos.add(elem);
    }

    public ArrayList<T> getDatos() {
        return datos;
    }

    public void ordenar() {
        Collections.sort(datos);
    }
}

