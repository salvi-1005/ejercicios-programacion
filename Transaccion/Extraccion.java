public class Extraccion extends Transaccion {

    private int importe;

    public Extraccion(CuentaBancaria cuenta, int importe) {
        super(cuenta);
        this.importe = importe;
    }

    @Override
    public void ejecutar() {
        cuenta.extraer(importe);
    }
}
