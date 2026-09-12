public class BuscarElemento<E> {
    
    private E[] array;
    private E elemento;

    public BuscarElemento(E[] array, E elemento) {
        this.array = array;
        this.elemento = elemento;
    }

    public E buscar() {
        for (E e : array) {
            if (e.equals(elemento)) {
                return e;
            }
        }
        return null;
    }
    
}
