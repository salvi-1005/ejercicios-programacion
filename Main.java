public class Main {
    import java.util.NoSuchElementException;

interface Secuencia<T> {
    int longitud();
    void agregarAdelante(T elem);
    void agregarAtras(T elem);
    void eliminar(int i);
    T obtener(int i);
    void modificarPosicion(int i, T elem);
    ListaEnlazada<T> copiar();
    Iterador<T> iterador();
    String toString();
}

interface Iterador<T> {
    boolean haySiguiente();
    boolean hayAnterior();
    T siguiente() throws NoSuchElementException;
    T anterior() throws NoSuchElementException;
}

class Nodo<T> {
    T elemento;
    Nodo<T> anterior;
    Nodo<T> siguiente;

    Nodo(T elem) {
        this.elemento = elem;
        this.anterior = null;
        this.siguiente = null;
    }
}

class ListaEnlazada<T> implements Secuencia<T> {
    private Nodo<T> primero;
    private Nodo<T> ultimo;
    private int size;

    ListaEnlazada() {
        this.primero = null;
        this.ultimo = null;
        this.size = 0;
    }

    public int longitud() {
        return size;
    }

    public void agregarAdelante(T elem) {
        Nodo<T> nuevoNodo = new Nodo<>(elem);
        if (primero == null) {
            primero = nuevoNodo;
            ultimo = nuevoNodo;
        } else {
            nuevoNodo.siguiente = primero;
            primero.anterior = nuevoNodo;
            primero = nuevoNodo;
        }
        size++;
    }

    public void agregarAtras(T elem) {
        Nodo<T> nuevoNodo = new Nodo<>(elem);
        if (ultimo == null) {
            primero = nuevoNodo;
            ultimo = nuevoNodo;
        } else {
            ultimo.siguiente = nuevoNodo;
            nuevoNodo.anterior = ultimo;
            ultimo = nuevoNodo;
        }
        size++;
    }

    public void eliminar(int i) {
        if (i < 0 || i >= size) {
            throw new IndexOutOfBoundsException("Posición inválida");
        }
        if (i == 0) {
            if (size == 1) {
                primero = null;
                ultimo = null;
            } else {
                primero = primero.siguiente;
                primero.anterior = null;
            }
        } else if (i == size - 1) {
            ultimo = ultimo.anterior;
            ultimo.siguiente = null;
        } else {
            Nodo<T> actual = primero;
            for (int j = 0; j < i; j++) {
                actual = actual.siguiente;
            }
            actual.anterior.siguiente = actual.siguiente;
            actual.siguiente.anterior = actual.anterior;
        }
        size--;
    }

    public T obtener(int i) {
        if (i < 0 || i >= size) {
            throw new IndexOutOfBoundsException("Posición inválida");
        }
        Nodo<T> actual = primero;
        for (int j = 0; j < i; j++) {
            actual = actual.siguiente;
        }
        return actual.elemento;
    }

    public void modificarPosicion(int i, T elem) {
        if (i < 0 || i >= size) {
            throw new IndexOutOfBoundsException("Posición inválida");
        }
        Nodo<T> actual = primero;
        for (int j = 0; j < i; j++) {
            actual = actual.siguiente;
        }
        actual.elemento = elem;
    }

    public ListaEnlazada<T> copiar() {
        ListaEnlazada<T> copia = new ListaEnlazada<>();
        Nodo<T> actual = primero;
        while (actual != null) {
            copia.agregarAtras(actual.elemento);
            actual = actual.siguiente;
        }
        return copia;
    }

    public Iterador<T> iterador() {
        return new ListaIterador();
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        Nodo<T> actual = primero;
        while (actual != null) {
            sb.append(actual.elemento);
            if (actual.siguiente != null) {
                sb.append(", ");
            }
            actual = actual.siguiente;
        }
        sb.append("]");
        return sb.toString();
    }

    private class ListaIterador implements Iterador<T> {
        private Nodo<T> actual;

        ListaIterador() {
            this.actual = primero;
        }

        public boolean haySiguiente() {
            return actual != null;
        }

        public boolean hayAnterior() {
            return actual != null && actual.anterior != null;
        }

        public T siguiente() {
            if (!haySiguiente()) {
                throw new NoSuchElementException("No hay elemento siguiente");
            }
            T elem = actual.elemento;
            actual = actual.siguiente;
            return elem;
        }

        public T anterior() {
            if (!hayAnterior()) {
                throw new NoSuchElementException("No hay elemento anterior");
            }
            actual = actual.anterior;
            return actual.elemento;
        }
    }
}

}
