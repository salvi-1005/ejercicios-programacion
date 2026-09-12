public abstract class Either<A, B> {

    public abstract boolean isLeft();
    public abstract boolean isRight();

    public abstract A getLeft();
    public abstract B getRight();

    //Constructores estáticos
    public static <A, B> Either<A, B> left(A value) {
        return new Left<>(value);
    }

    public static <A, B> Either<A, B> right(B value) {
        return new Right<>(value);
    }

    //Clases internas

    private static class Left<A, B> extends Either<A, B> {
        private final A value;

        public Left(A value) {
            this.value = value;
        }

        public boolean isLeft() { return true; }
        public boolean isRight() { return false; }

        public A getLeft() { return value; }

        public B getRight() {
            throw new RuntimeException("No es Right");
        }
    }

    private static class Right<A, B> extends Either<A, B> {
        private final B value;

        public Right(B value) {
            this.value = value;
        }

        public boolean isLeft() { return false; }
        public boolean isRight() { return true; }

        public A getLeft() {
            throw new RuntimeException("No es Left");
        }

        public B getRight() { return value; }
    }
}