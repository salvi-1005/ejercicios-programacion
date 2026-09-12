public class Matriz<E> {
    
    private E[][] matriz;

    @SuppressWarnings("unchecked")
    public Matriz() {
        this.matriz = (E[][]) new Object[0][0];  
    }

    public E[][] getMatriz() {
        return matriz;
    }
    
    @SuppressWarnings("unchecked")
    public void agregarFila(E[] fila) {
        if (matriz.length > 0 && fila.length != matriz[0].length) {
            throw new IllegalArgumentException("La fila debe tener el mismo número de columnas que la matriz");
        }

        if (matriz.length == 0) {
            matriz = (E[][]) new Object[1][fila.length];
            System.arraycopy(fila, 0, matriz[0], 0, fila.length);
            return;
        }

        E[][] nuevaMatriz = (E[][]) new Object[matriz.length + 1][matriz[0].length];

        for (int i = 0; i < matriz.length; i++) {
            System.arraycopy(matriz[i], 0, nuevaMatriz[i], 0, matriz[i].length);
        }

        nuevaMatriz[matriz.length] = fila;
        matriz = nuevaMatriz;
    }


    @SuppressWarnings("unchecked")
    public void agregarColumna(E[] columna) {
        if (matriz.length > 0 && columna.length != matriz.length) {
            throw new IllegalArgumentException("La columna debe tener el mismo número de filas que la matriz");
        }

        if (matriz.length == 0) {
            matriz = (E[][]) new Object[columna.length][1];
            for (int i = 0; i < columna.length; i++) {
                matriz[i][0] = columna[i];
            }
            return;
        }

        E[][] nuevaMatriz = (E[][]) new Object[matriz.length][matriz[0].length + 1];

        for (int i = 0; i < matriz.length; i++) {
            System.arraycopy(matriz[i], 0, nuevaMatriz[i], 0, matriz[i].length);
            nuevaMatriz[i][matriz[0].length] = columna[i];
        }

        matriz = nuevaMatriz;
    }

    @SuppressWarnings("unchecked")
    public void eliminarFila(int index){
        if (index < 0 || index >= matriz.length) {
            throw new IndexOutOfBoundsException("Índice fuera de rango");
        }
        E[][] nuevaMatriz = (E[][]) new Object[matriz.length - 1][matriz[0].length];
        for (int i = 0, j = 0; i < matriz.length; i++) {
            if (i != index) {
                System.arraycopy(matriz[i], 0, nuevaMatriz[j], 0, matriz[i].length);
                j++;
            }
        }
        matriz = nuevaMatriz;
    }

    @SuppressWarnings("unchecked")
    public void eliminarColumna(int index){
        if (index < 0 || index >= matriz[0].length) {
            throw new IndexOutOfBoundsException("Índice fuera de rango");
        }
        E[][] nuevaMatriz = (E[][]) new Object[matriz.length][matriz[0].length - 1];
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0, k = 0; j < matriz[i].length; j++) {
                if (j != index) {
                    nuevaMatriz[i][k] = matriz[i][j];
                    k++;
                }
            }
        }
        matriz = nuevaMatriz;
    }

    public void cambiarOrdenFilas(int index1, int index2){
        if (index1 < 0 || index1 >= matriz.length || index2 < 0 || index2 >= matriz.length) {
            throw new IndexOutOfBoundsException("Índice fuera de rango");
        }
        E[] temp = matriz[index1];
        matriz[index1] = matriz[index2];
        matriz[index2] = temp;
    }

    public void cambiarOrdenColumnas(int index1, int index2){
        if (index1 < 0 || index1 >= matriz[0].length || index2 < 0 || index2 >= matriz[0].length) {
            throw new IndexOutOfBoundsException("Índice fuera de rango");
        }
        for (int i = 0; i < matriz.length; i++) {
            E temp = matriz[i][index1];
            matriz[i][index1] = matriz[i][index2];
            matriz[i][index2] = temp;
        }
    }

    public void ordenarFilasPorColumna(int columnIndex){
        for (int i = 0; i < matriz.length - 1; i++) {
            for (int j = 0; j < matriz.length - i - 1; j++) {
                if (matriz[j][columnIndex].toString().compareTo(matriz[j + 1][columnIndex].toString()) > 0) {
                    cambiarOrdenFilas(j, j + 1);
                }
            }
        }
    }

    public void imprimirMatriz() {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }

}
