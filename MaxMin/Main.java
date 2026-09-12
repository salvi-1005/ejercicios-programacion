import java.util.Arrays;

public class Main {
    
    public static void main(String[] args) {
        
        MaxMin m = new MaxMin("3 4 5 6");

        int[] resultado = m.devolverMaxMin();

        System.out.println(Arrays.toString(resultado));

}
}