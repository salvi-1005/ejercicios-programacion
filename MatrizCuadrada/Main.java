public class Main {
    
    public static void main(String[] args) {
        
        MatrizCuadrada<Integer> m = new MatrizCuadrada<>(new Integer[][]{
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        });
        System.out.println(m.esMatrizCuadrada());

        System.out.println(m.transpuesta());

        System.out.println(m.sumarMatrices(m.transpuesta()));
    }
}
