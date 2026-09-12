public abstract class Automovil extends VehiculoMotorizado implements CapacidadLimite {
    
    protected int maximoDePasajeros;

    public Automovil(String fabricante, String modelo, int añoDeFabricacion, double kilometraje, int max){
        super(fabricante, modelo, añoDeFabricacion, kilometraje);
        this.maximoDePasajeros = max;
    }

    public abstract int getMaximoDePasajeros();

    @Override
    public String toString() {
        return "Motocicleta: " + modelo + " - Motocicleta: " + maximoDePasajeros;
    }

}
