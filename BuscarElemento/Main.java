public class Main {
    
    public static void main(String[] args) {
        
        BuscarElemento<Integer> b = new BuscarElemento<Integer>(new Integer[]{1, 2, 3, 4, 5}, 3);
        System.out.println(b.buscar());
    }
}