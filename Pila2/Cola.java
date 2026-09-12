import java.util.ArrayList;

public class Cola<E> implements Pila<E>{

    private ArrayList<E> datos;
    
    public Cola(){
        datos = new ArrayList<>();
    }
    
    
    public void encolar(E elemento){
        datos.add(elemento);
    }

    public E desencolar(){
        if (isEmpty()){
            return null;
        }
        return datos.remove(0);
    }

    public E peek(){
        if (isEmpty()) {
            return null;
        }
        return datos.get(0);
    }

    public boolean isEmpty(){
        return datos.isEmpty();
    }

    public int size(){
        return datos.size();
    }
}
