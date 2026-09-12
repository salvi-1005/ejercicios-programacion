import java.util.Arrays;

public class Main {
    
    public static void main(String[] args) {
        
        Unicos<Integer> u = new Unicos<>(new Integer[]{3, 3, 4, 6});
        System.out.println(Arrays.toString(u.sacarRepetidos()));

    }
}