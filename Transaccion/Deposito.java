public class Deposito extends Transaccion {

    private int importe;

    public Deposito(CuentaBancaria cuenta, int importe) {
        super(cuenta);
        this.importe = importe;
    }

    @Override
    public void ejecutar() {
        cuenta.depositar(importe);
    }
}
