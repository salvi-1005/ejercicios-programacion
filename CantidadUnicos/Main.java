public class Main {
    
    public static void main(String[] args) {
        
        CantidadUnicos<Integer> c = new CantidadUnicos<>(new Integer[]{3, 3, 4, 6});
        System.out.println(c.contarUnicos());
    }
}
