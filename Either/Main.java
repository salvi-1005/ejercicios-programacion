public class Main {
    public static void main(String[] args){
        
        Lista<Integer> lista = Lista.cons(1, Lista.cons(2, Lista.cons(3, Lista.vacia())));

        System.out.println(lista.cabeza()); // 1
    }
}
