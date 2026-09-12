public class Camion extends VehiculoMotorizado implements CapacidadLimite{
    
    private int maximoDePasajeros;
    private int cantRemolques;

    public Camion(String fabricante, String modelo, int añoDeFabricacion, double kilometraje, int max, int rem){
        super(fabricante, modelo, añoDeFabricacion, kilometraje);
        this.maximoDePasajeros = max;
        this.cantRemolques = rem;
    }

    public int getMaximoDePasajeros(){
        return this.maximoDePasajeros;
    }

    public boolean esSeguro() {
        return maximoDePasajeros <= MAX_CAMION;
    }

    public int getCantRemolques(){
        return this.cantRemolques;
    }

    @Override
    public String toString() {
        return "Camion: " + modelo + " - Seguridad: " + esSeguro();
    }

}
