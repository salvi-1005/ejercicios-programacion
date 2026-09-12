public class Main {
    
    public static void main(String[] args) {
        
        ArrayListContainer<Integer> a = new ArrayListContainer<>();
        
        a.add(1);
        a.add(2);
        a.add(3);
        
        System.out.println(a.getInicial());
        System.out.println(a.getFinal());
        System.out.println("Size: " + a.size());
        System.out.println("Sum: " + a.sumar());
        System.out.println("Average: " + a.getPromedio());
        
    }

}
