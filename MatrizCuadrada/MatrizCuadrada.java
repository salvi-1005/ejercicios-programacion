public class MatrizCuadrada<E extends Number> {
    
    private E[][] matriz;

    public MatrizCuadrada(E[][] matriz) {
        this.matriz = matriz;
    }

    public boolean esMatrizCuadrada() {
        int filas = matriz.length;
        for (E[] fila : matriz) {
            if (fila.length != filas) {
                return false;
            }
        }
        return true;
    }

    public MatrizCuadrada<E> transpuesta() {
        if (!esMatrizCuadrada()) {
            throw new IllegalStateException("La matriz no es cuadrada");
        }
        int n = matriz.length;
        @SuppressWarnings("unchecked")
        E[][] transpuesta = (E[][]) new Number[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                transpuesta[j][i] = matriz[i][j];
            }
        }
        return new MatrizCuadrada<>(transpuesta);
    }
    

    public MatrizCuadrada<E> sumarMatrices(MatrizCuadrada<E> otra) {
        if (!esMatrizCuadrada() || !otra.esMatrizCuadrada() || matriz.length != otra.matriz.length) {
            throw new IllegalStateException("Las matrices no son cuadradas o no tienen el mismo tamaño");
        }
        int n = matriz.length;
        @SuppressWarnings("unchecked")
        E[][] resultado = (E[][]) new Number[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                resultado[i][j] = sumarElementos(matriz[i][j], otra.matriz[i][j]);
            }
        }
        return new MatrizCuadrada<>(resultado);
    }

    @SuppressWarnings("unchecked")
    public E sumarElementos(E a, E b) {
        if (a instanceof Integer && b instanceof Integer) {
            return (E) Integer.valueOf(((Integer) a) + ((Integer) b));
        } else if (a instanceof Double && b instanceof Double) {
            return (E) Double.valueOf(((Double) a) + ((Double) b));
        } else if (a instanceof Float && b instanceof Float) {
            return (E) Float.valueOf(((Float) a) + ((Float) b));
        } else if (a instanceof Long && b instanceof Long) {
            return (E) Long.valueOf(((Long) a) + ((Long) b));
        } else {
            throw new IllegalArgumentException("Tipos de números no soportados");
        }

    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                sb.append(matriz[i][j]).append(" ");
            }
            sb.append("\n");
        }

        return sb.toString();
    }
}