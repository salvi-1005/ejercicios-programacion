public class ConsultaSaldo extends Transaccion {

    public ConsultaSaldo(CuentaBancaria cuenta) {
        super(cuenta);
    }

    @Override
    public void ejecutar() {
        System.out.println(cuenta.consultarSaldo());
    }
}