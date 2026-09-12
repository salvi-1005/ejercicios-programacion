public class Main {
    
    public static void main(String[] args) {
        
        ArrayListRest<Integer> a = new ArrayListRest<Integer>();

        a.add(1);
        a.add(2);
        a.add(3);

        System.out.println(a.rest());
    }
}