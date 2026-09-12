import java.util.ArrayList;

public class ColaPrioridad<E> {
    // Clase interna para asociar dato y prioridad
    private class Elemento<T> {
        T dato;
        int prioridad;
        Elemento(T d, int p) { this.dato = d; this.prioridad = p; }
    }

    private ArrayList<Elemento<E>> elementos;

    public ColaPrioridad() {
        this.elementos = new ArrayList<>(); // Inicialización dinámica [6, 7]
    }

    public void enqueuePriority(E item, int priority) {
        elementos.add(new Elemento<>(item, priority)); // Agrega al final [2]
    }

    public E dequeueHigh() {
        if (elementos.isEmpty()) throw new RuntimeException("Cola vacía"); // Precondición [10]
        
        int indiceMayor = 0;
        // Búsqueda del elemento con mayor prioridad [4]
        for (int i = 1; i < elementos.size(); i++) {
            if (elementos.get(i).prioridad > elementos.get(indiceMayor).prioridad) {
                indiceMayor = i;
            }
        }
        return elementos.remove(indiceMayor).dato; // Elimina y retorna [9]
    }

    public E peek() {
        if (elementos.isEmpty()) throw new RuntimeException("Cola vacía");
        int indiceMayor = 0;
        // Búsqueda del elemento con mayor prioridad [4]
        for (int i = 1; i < elementos.size(); i++) {
            if (elementos.get(i).prioridad > elementos.get(indiceMayor).prioridad) {
                indiceMayor = i;
            }
        }
        return elementos.get(indiceMayor).dato; // Elimina y retorna [9]
    }
        

    public int size() {
        return elementos.size(); // Propiedad de la colección [13]
    }

    public boolean isEmpty(){
        return elementos.isEmpty();
    }
    
    // Otros métodos: peek(), isEmpty() siguiendo la misma lógica
}