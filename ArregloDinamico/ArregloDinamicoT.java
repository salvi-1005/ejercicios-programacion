public class ArregloDinamicoT<T> {

    private T[] arreglo;
    private int size;

    @SuppressWarnings("unchecked")
    public ArregloDinamicoT() {
        this.arreglo = (T[]) new Object[0];
        this.size = 0;
    }

    public void agregar(T elemento) {
        if (size == arreglo.length) {
            redimensionar();
        }
        arreglo[size] = elemento;
        size++;
    }

    @SuppressWarnings("unchecked")
    private void redimensionar() {
        int nuevaCapacidad;

        if (arreglo.length == 0) {
            nuevaCapacidad = 1;              
        } else {
            nuevaCapacidad = arreglo.length * 2;
        }

        T[] nuevo = (T[]) new Object[nuevaCapacidad];

        for (int i = 0; i < size; i++) {
            nuevo[i] = arreglo[i];
        }

        arreglo = nuevo;
    }


    public T obtener(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Índice fuera de rango");
        }
        return arreglo[index];
    }

    public int getSize() {
        return size;
    }
    
}
