public class Main {
    public static void main(String[] args) {

        CuentaCorriente m = new CuentaCorriente(500, 0, 0);
        System.out.println(m.saldo());
        m.deposito(8000);
        System.out.println(m.saldo());
        m.extraccion(1000);
        System.out.println(m.saldo());
        System.out.println(m.cantidadOperaciones());
        m.extraccion(10000);
        System.out.println(m.cantidadExtraccionesInvalidas());
    }
}
