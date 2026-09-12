import java.util.Arrays;

public class PilaArray<E> {

    private E[] datos;
    private int tope;        // cantidad de elementos
    private int incremento; // cuánto crece el array

    @SuppressWarnings("unchecked")
    public PilaArray(int capacidadInicial, int incremento) {
        this.datos = (E[]) new Object[capacidadInicial]; // casting necesario
        this.tope = 0;
        this.incremento = incremento;
    }

    // PUSH
    public void push(E elemento) {
        if (tope == datos.length) {
            agrandar();
        }
        datos[tope] = elemento;
        tope++;
    }

    // POP
    public E pop() {
        if (isEmpty()) {
            throw new RuntimeException("Pila vacía");
        }
        tope--;
        return datos[tope];
    }

    // SIZE
    public int size() {
        return tope;
    }

    // VACÍA
    public boolean isEmpty() {
        return tope == 0;
    }

    // VER TOPE (extra útil)
    public E peek() {
        if (isEmpty()) {
            throw new RuntimeException("Pila vacía");
        }
        return datos[tope - 1];
    }

    // AGRANDAR ARRAY
    private void agrandar() {
        int nuevoTam = datos.length + incremento;
        datos = Arrays.copyOf(datos, nuevoTam);
    }
}
