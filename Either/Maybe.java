public abstract class Maybe<A> {

    public abstract boolean isPresent();
    public abstract A get();

    public static <A> Maybe<A> just(A value) {
        return new Just<>(value);
    }

    public static <A> Maybe<A> nothing() {
        return new Nothing<>();
    }

    //Clases internas

    private static class Just<A> extends Maybe<A> {
        private final A value;

        public Just(A value) {
            this.value = value;
        }

        public boolean isPresent() { return true; }

        public A get() { return value; }
    }

    private static class Nothing<A> extends Maybe<A> {

        public boolean isPresent() { return false; }

        public A get() {
            throw new RuntimeException("No hay valor");
        }
    }
}
