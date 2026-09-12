public class Wrapper<T> {

    private T clase;

    public Wrapper(T cla){
        this.clase = cla;
    }
    
    public void setClase(T cla){
        this.clase = cla;
    }

    public T getClase(){
        return clase;
    }

    public void mostrar() {
    System.out.println(clase.toString());
    }

}