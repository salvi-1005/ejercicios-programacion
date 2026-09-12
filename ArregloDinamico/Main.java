public class Main {
    
    public static void main(String[] args) {
        
        ArregloDinamicoT<Integer> a = new Cola<Integer>();

        a.agregar(1);
        a.agregar(2);
        a.agregar(3);
        a.agregar(4);

        System.out.println(a.getSize());

        for (int i = 0; i < a.getSize(); i++) {
            System.out.println(a.obtener(i));
        }


    }
}
