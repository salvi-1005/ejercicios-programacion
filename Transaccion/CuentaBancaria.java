public class CuentaBancaria {

    private int saldo;
    public int numeroDeCuenta;

    public CuentaBancaria(int saldo, int numeroDeCuenta){
        this.saldo = saldo;
        this.numeroDeCuenta = numeroDeCuenta;
    }

    public int getNumeroDeCuenta(){
        return numeroDeCuenta;
    }

    public int consultarSaldo(){
        return this.saldo;
    }

    public void extraer(int importe){
        this.saldo -= importe;
    }

    public void depositar(int importe){
        this.saldo += importe;
    }
}
