public class Main {
    public static void main(String[] args){

        Pila<Object> p = new Cola<>();
        p.encolar(10);
        p.encolar(4);
        p.encolar("Hola");

        System.out.println(p.isEmpty());
    
        PilaArray p2 = new PilaArray(1,2);
        p2.apilar(40);
        p2.apilar(50);
        p2.apilar(60);
        p2.apilar(70);
        System.out.println(p2.desapilar());
        System.out.println(p.desencolar());

    }
}
