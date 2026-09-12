public class ColaArray<E> {

    private E[] datos;
    private int inicio;
    private int fin;
    private int size;
    private int capacidad;

    @SuppressWarnings("unchecked")
    public ColaArray(int capacidadInicial) {
        this.capacidad = capacidadInicial;
        this.datos = (E[]) new Object[capacidad];
        this.inicio = 0;
        this.fin = 0;
        this.size = 0;
    }

    // ENQUEUE
    public void enqueue(E elemento) {
        if (size == capacidad) {
            agrandar();
        }

        datos[fin] = elemento;
        fin = (fin + 1) % capacidad;
        size++;
    }

    // DEQUEUE
    public E dequeue() {
        if (isEmpty()) {
            throw new RuntimeException("Cola vacía");
        }

        E elemento = datos[inicio];
        inicio = (inicio + 1) % capacidad;
        size--;

        return elemento;
    }

    // PEEK
    public E peek() {
        if (isEmpty()) {
            throw new RuntimeException("Cola vacía");
        }
        return datos[inicio];
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
    @SuppressWarnings("unchecked")
    private void agrandar() {
        int nuevaCapacidad = capacidad * 2;
        E[] nuevo = (E[]) new Object[nuevaCapacidad];

        // Copiamos en orden correcto
        for (int i = 0; i < size; i++) {
            nuevo[i] = datos[(inicio + i) % capacidad];
        }

        datos = nuevo;
        inicio = 0;
        fin = size;
        capacidad = nuevaCapacidad;
    }
}

