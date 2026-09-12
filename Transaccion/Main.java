public class Main {
    public static void main(String[] args) {
        CuentaBancaria c = new CuentaBancaria(1000, 123);
 

        Transaccion t1 = new ConsultaSaldo(c);
        Transaccion t2 = new Deposito(c, 500);
        Transaccion t3 = new Extraccion(c, 200);

        t1.ejecutar();

        t2.ejecutar();
        new ConsultaSaldo(c).ejecutar();

        t3.ejecutar();
        new ConsultaSaldo(c).ejecutar();

    }
}
                                               