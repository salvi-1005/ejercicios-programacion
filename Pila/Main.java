public class Main {
    
    public static void main(String[] args){

        Pila<Object> p = new Pila<>();
        p.push(10);
        p.push(4);
        p.push("Hola");

        System.out.println(p.size());
        System.out.println(p.isEmpty());
        System.out.println(p.peek());

        Pila<Object> p2 = new Pila<>();
        p2.push(40);
        System.out.println(p2.pop());
        System.out.println(p2.peek());

        

    }

}