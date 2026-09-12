import java.util.ArrayList;

public class ArrayListContainer<T extends Number> implements Estadistica<T> {
    
    private ArrayList<T> datos;

    public ArrayListContainer(){
        datos = new ArrayList<>();
    }
    
    public T getInicial(){
        if(datos.size() == 0) return null;
        return datos.get(0);
    }

    public T getFinal(){
        if(datos.size() == 0) return null;
        return datos.get(datos.size() - 1);
    }

    public int size(){
        return datos.size();
    }

    public int sumar(){
        int suma = 0;
        for(T dato : datos){
            if(dato instanceof Number){
                suma += ((Number) dato).intValue();
            }
        }
        return suma;
    }

    public double getPromedio(){
        if(datos.size() == 0) return 0;
        return sumar() / datos.size();
    }

    public void add(T dato){
        datos.add(dato);
    }

    public T get(int index){
        return datos.get(index);
    }

    public void remove(int index){
        datos.remove(index);
    }

    public boolean isEmpty(){
        return datos.isEmpty();
    }

}
