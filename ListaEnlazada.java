package aed;

import java.util.NoSuchElementException;

public class ListaEnlazada<T> implements Secuencia<T> {
    private Node<T> primero;
    private Node<T> ultimo;
    private int size;

    private static class Node<T> {
        T elemento;
        Node<T> siguiente;
        Node<T> anterior;

        Node(T elemento, Node<T> anterior, Node<T> siguiente) {
            this.elemento = elemento;
            this.anterior = anterior;
            this.siguiente = siguiente;
        }
    }

    public ListaEnlazada() {
        primero = null;
        ultimo = null;
        size = 0;
    }

    public ListaEnlazada(ListaEnlazada<T> lista) {
        this();
        Node<T> corriente = lista.primero;
        while (corriente != null) {
            agregarAtras(corriente.elemento);
            corriente = corriente.siguiente;
        }
    }

    public int longitud() {
        return size;
    }

    public void agregarAdelante(T elem) {
        Node<T> newNode = new Node<>(elem, null, primero);
        if (primero == null) {
            ultimo = newNode;
        } else {
            primero.anterior = newNode;
        }
        primero = newNode;
        size++;
    }

    public void agregarAtras(T elem) {
        Node<T> newNode = new Node<>(elem, ultimo, null);
        if (ultimo == null) {
            primero = newNode;
        } else {
            ultimo.siguiente = newNode;
        }
        ultimo = newNode;
        size++;
    }

    public T obtener(int i) {
        if (i < 0 || i >= size) {
            throw new IndexOutOfBoundsException("Posición inválida");
        }
        Node<T> actual = primero;
        for (int j = 0; j < i; j++) {
            actual = actual.siguiente;
        }
        return actual.elemento;
    }

    public void eliminar(int i) {
        if (i < 0 || i >= longitud()) {
            throw new IndexOutOfBoundsException("Índice fuera de rango");
        }

        if (i == 0) {
            primero = primero.siguiente;
            if (primero != null) {
                primero.anterior = null;
            } else {
                ultimo = null;
            }
        } else {
            Node<T> actual = primero;
            for (int j = 0; j < i - 1; j++) {
                actual = actual.siguiente;
            }
            actual.siguiente = actual.siguiente.siguiente;
            if (actual.siguiente == null) {
                ultimo = actual;
            } else {
                actual.siguiente.anterior = actual;
            }
        }
        size--;
    }

    public void modificarPosicion(int i, T elem) {
        if (i < 0 || i >= size) {
            throw new IndexOutOfBoundsException("Posición inválida");
        }
        Node<T> actual = primero;
        for (int j = 0; j < i; j++) {
            actual = actual.siguiente;
        }
        actual.elemento = elem;
    }

    public ListaEnlazada<T> copiar() {
        return new ListaEnlazada<>(this);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        Node<T> actual = primero;
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

    private class ListaEnlazadaIterador implements Iterador<T> {
        private Node<T> corriente;
        private Node<T> previo; 

        public ListaEnlazadaIterador(Node<T> primerNodo) {
            this.corriente = primerNodo;
            this.previo = null;
        }

        public boolean haySiguiente() {
            return corriente != null;
        }

        public boolean hayAnterior() {
            return previo != null;
        }

        public T siguiente() {
            if (!haySiguiente()) {
                throw new NoSuchElementException();
            }
            T elem = corriente.elemento;
            previo = corriente;
            corriente = corriente.siguiente;
            return elem;
        }

        public T anterior() {
            if (!hayAnterior()) {
                throw new NoSuchElementException();
            }
            corriente = previo;
            previo = corriente.anterior;
            return corriente.elemento;
        }
    }

    public Iterador<T> iterador() {
        return new ListaEnlazadaIterador(primero);
    }
}

