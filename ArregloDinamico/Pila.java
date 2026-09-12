public class Pila<T> extends ArregloDinamicoT<T> {

    public void push(T elemento) {
        agregar(elemento);
    }

    public T pop() {
        if (getSize() == 0) {
            throw new IllegalStateException("La pila está vacía");
        }
        T elemento = obtener(getSize() - 1);
        // Eliminar el elemento de la pila
        // No es necesario eliminar físicamente el elemento, solo reducir el tamaño
        return elemento;
    }
    
}
