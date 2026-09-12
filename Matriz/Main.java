public class Main {
    
    public static void main(String[] args) {
        
        Matriz<Integer> m = new Matriz<Integer>();

        m.agregarFila(new Integer[]{1, 2, 3});
        m.agregarFila(new Integer[]{5, 6, 7,});
        m.agregarFila(new Integer[]{9, 10, 11});
        m.agregarColumna(new Integer[]{4, 8, 12});

        m.imprimirMatriz();

        m.cambiarOrdenFilas(1,2);
        m.imprimirMatriz();

        }

    
}

