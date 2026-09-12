public class CuentaBancaria implements Medible{
    
    private float saldo;

    public CuentaBancaria(){
        this.saldo = 0;
    }

    @Override
    public float obtenerMedida(){
        return this.saldo;
    }

    @Override
    public float incrementar(float inc){
        return saldo + inc;
    }
    
    @Override
    public float decrementar(float dec){
        try {
            if (this.saldo - dec < 0) {
                throw new ArithmeticException();
            }
        }
        catch (ArithmeticException e) {
            System.out.println("Error: El saldo no puede ser negativo");
        } finally {
            System.out.println("Finalizando proceso.");
        }
        return this.saldo - dec;
    }

}
