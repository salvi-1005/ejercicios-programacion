public class Main {
    
    public static void main(String[] args){
        ColaPrioridad<Object> cola = new ColaPrioridad<>();

        cola.enqueuePriority(5, 1);
        cola.enqueuePriority(1, 2);
        cola.enqueuePriority(10, 3);

        System.out.println(cola.peek());

        while (!cola.isEmpty()) {
            System.out.println(cola.dequeueHigh());
        }

        System.out.println(cola.size());
    }

}
