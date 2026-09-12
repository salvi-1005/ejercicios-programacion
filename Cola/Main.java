public class Main {
    
    public static void main(String[] args){

        Cola<Object> p = new Cola<>();
        p.encolar(10);
        p.encolar(4);
        p.encolar("Hola");

        System.out.println(p.size());
        System.out.println(p.isEmpty());
        System.out.println(p.peek());

        Cola<Object> p2 = new Cola<>();
        p2.encolar(40);
        System.out.println(p2.desencolar());
        System.out.println(p2.peek());
        System.out.println(p.desencolar());

        

    }

}