import java.util.ArrayList;

public class ArrayListRest<E> {
    
    private ArrayList<E> list;

    public ArrayListRest(){
        this.list = new ArrayList<>();
    }

    public void add(E element){
        list.add(element);
    }

    public void eliminar(E element){
        list.remove(element);
    }

    public ArrayList<E> rest(){
        if (list.isEmpty()) {
            return new ArrayList<>();
        }
        return new ArrayList<>(list.subList(1, list.size()));
    }
    
}
