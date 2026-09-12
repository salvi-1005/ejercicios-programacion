public class Cola<T> extends ArregloDinamicoT<T> {

    public void enqueue(T elemento) {
        agregar(elemento);
    }

    public T dequeue() {
        if (getSize() == 0) {
            throw new IllegalStateException("La cola está vacía");
        }
        T elemento = obtener(0);
        // Eliminar el elemento de la cola
        // No es necesario eliminar físicamente el elemento, solo reducir el tamaño
        return elemento;
    }

    
}
