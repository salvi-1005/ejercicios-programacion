public abstract class Lista<A> {

    public abstract boolean esVacia();
    public abstract A cabeza();
    public abstract Lista<A> cola();

    //Constructores

    public static <A> Lista<A> vacia() {
        return new Vacia<>();
    }

    public static <A> Lista<A> cons(A cabeza, Lista<A> cola) {
        return new Cons<>(cabeza, cola);
    }

    //Clases internas

    private static class Vacia<A> extends Lista<A> {

        public boolean esVacia() { return true; }

        public A cabeza() {
            throw new RuntimeException("Lista vacía");
        }

        public Lista<A> cola() {
            throw new RuntimeException("Lista vacía");
        }
    }

    private static class Cons<A> extends Lista<A> {
        private final A cabeza;
        private final Lista<A> cola;

        public Cons(A cabeza, Lista<A> cola) {
            this.cabeza = cabeza;
            this.cola = cola;
        }

        public boolean esVacia() { return false; }

        public A cabeza() { return cabeza; }

        public Lista<A> cola() { return cola; }
    }
}
