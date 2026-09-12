public abstract class Transaccion {

    protected CuentaBancaria cuenta;

    public Transaccion(CuentaBancaria cuenta) {
        this.cuenta = cuenta;
    }

    public void mostrarNumeroDeCuenta() {
        System.out.println(cuenta.getNumeroDeCuenta());
    }

    public abstract void ejecutar();
}
