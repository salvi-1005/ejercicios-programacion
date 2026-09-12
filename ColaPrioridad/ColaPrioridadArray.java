import java.util.Arrays;

public class ColaPrioridadArray<E extends Comparable<E>> {

    private E[] datos;
    private int size;
    private int capacidad;

    @SuppressWarnings("unchecked")
    public ColaPrioridadArray(int capacidadInicial) {
        this.capacidad = capacidadInicial;
        this.datos = (E[]) new Comparable[capacidad];
        this.size = 0;
    }

    // ENQUEUE
    public void enqueuePriority(E elemento) {
        if (size == capacidad) {
            agrandar();
        }
        datos[size] = elemento;
        size++;
    }

    // DEQUEUE HIGH (mayor prioridad)
    public E dequeueHigh() {
        if (isEmpty()) {
            throw new RuntimeException("Cola vacía");
        }

        int indiceMax = 0;

        for (int i = 1; i < size; i++) {
            if (datos[i].compareTo(datos[indiceMax]) > 0) {
                indiceMax = i;
            }
        }

        E resultado = datos[indiceMax];

        // Corrimiento para eliminar
        for (int i = indiceMax; i < size - 1; i++) {
            datos[i] = datos[i + 1];
        }

        size--;
        return resultado;
    }

    // PEEK (sin eliminar)
    public E peek() {
        if (isEmpty()) {
            throw new RuntimeException("Cola vacía");
        }

        int indiceMax = 0;

        for (int i = 1; i < size; i++) {
            if (datos[i].compareTo(datos[indiceMax]) > 0) {
                indiceMax = i;
            }
        }

        return datos[indiceMax];
    }

    // SIZE
    public int size() {
        return size;
    }

    // EMPTY
    public boolean isEmpty() {
        return size == 0;
    }

    // AGRANDAR ARRAY
    private void agrandar() {
        capacidad *= 2;
        datos = Arrays.copyOf(datos, capacidad);
    }
}
