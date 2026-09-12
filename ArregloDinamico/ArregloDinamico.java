public class ArregloDinamico {
    
    private int[] arreglo;
    private int size;

    public ArregloDinamico(){
        this.arreglo = new int[0];
        this.size = 0;
    }

    public void agregar(int elemento){
        if (size == arreglo.length) {
            int[] nuevoArreglo = new int[arreglo.length * 2];
            System.arraycopy(arreglo, 0, nuevoArreglo, 0, arreglo.length);
            arreglo = nuevoArreglo;
        }
        arreglo[size] = elemento;
        size++;
    }

    public int get(int index){
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Índice fuera de rango");
        }
        return arreglo[index];
    }

    public int size(){
        return size;
    }
}
