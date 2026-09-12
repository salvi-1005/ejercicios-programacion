public class Main {
    
    public static void main(String[] args) {
        
        CuentaSuma c = new CuentaSuma(new int[]{1, -2, 3, -4, 5});
        ParAB<Integer, Integer> resultado = c.devolverPar();
        System.out.println(resultado);
    }
}