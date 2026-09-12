import java.util.ArrayList;

public abstract class Sort<T extends Comparable<T>> {
    
    protected ArrayList<T> datos;
    protected int comparaciones;
    protected int intercambios;

    public Sort(){
        datos = new ArrayList<T>();
        this.comparaciones = 0;
        this.intercambios = 0;

    }
    
    public ArrayList<T> getDatos() {
        return datos;
    }

    public int getComparaciones() {
        return comparaciones;
    }

    public int getIntercambios() {
        return intercambios;
    }

    public abstract void algoritmo();

    public void agregar(T elemento){
        datos.add(elemento);
    }

    protected boolean comparar(int i, int j){
        comparaciones += 1;
        return datos.get(i).compareTo(datos.get(j)) > 0;
    }

    protected void intercambiar(int i, int j){
        intercambios += 1;
        T temp = datos.get(i);
        datos.set(i, datos.get(j));
        datos.set(j, temp);

    }
}
