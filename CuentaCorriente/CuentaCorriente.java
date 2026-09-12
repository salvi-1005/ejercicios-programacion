public class CuentaCorriente {
    
    private int saldo;
    private int cantOperaciones;
    private int operacionesInvalidas;

    public CuentaCorriente(int saldo, int cantOperaciones, int operacionesInvalidas) {
        this.saldo = saldo;
        this.cantOperaciones = cantOperaciones;
        this.operacionesInvalidas = operacionesInvalidas;
    }

    public int saldo(){
        return this.saldo;
    }

    public void deposito(float imp){
        this.cantOperaciones += 1;
        this.saldo += imp;
    }

    public void extraccion(float imp){
        if (this.saldo >= imp){
            this.cantOperaciones += 1;
            this.saldo -= imp;
        }

        else {
            this.operacionesInvalidas += 1;
            System.out.println("No hay suficiente dinero");
        }
    }

    public int cantidadOperaciones(){
        return this.cantOperaciones;
    }

    public int cantidadExtraccionesInvalidas(){
        return this.operacionesInvalidas;
    }

}
