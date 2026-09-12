import java.util.ArrayList;

public class Pila<E> {

    private ArrayList<E> datos;
    
    public Pila(){
        datos = new ArrayList<>();
    }
    
    //Apilar
    public void push(E elemento){
        datos.add(elemento);
    }


    //Desapilar
    public E pop(){
        if (isEmpty()) {return null;}
        return datos.removeLast(); //datos.remove(datos.size()-1);
    }


    //Ver tope sin quitarlo
    public E peek(){
        if (isEmpty()) {return null;}
        return datos.get(datos.size()-1);
    }


    //¿Está vacía?
    public boolean isEmpty(){
        return datos.isEmpty();
    }


    //Cantidad de elementos
    public int size(){
        return datos.size();
    }


    public String toString(){
        return ("Media pila");
    }

}
