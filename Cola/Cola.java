import java.util.ArrayList;

public class Cola<E> {

    private ArrayList<E> datos;
    
    public Cola(){
        datos = new ArrayList<>();
    }
    
    //Apilar
    public void encolar(E elemento){
        datos.add(elemento);
    }


    //Desapilar
    public E desencolar(){
        if (isEmpty()){
            return null;
        }
        return datos.remove(0);
    }


    //Ver tope sin quitarlo
    public E peek(){
        if (isEmpty()) {
            return null;
        }
        return datos.get(0);
    }


    //¿Está vacía?
    public boolean isEmpty(){
        return datos.isEmpty();
    }


    //Cantidad de elementos
    public int size(){
        return datos.size();
    }
}
