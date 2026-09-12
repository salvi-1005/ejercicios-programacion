public class Motocicleta extends VehiculoMotorizado {
    
    private String uso;

    public Motocicleta(String fabricante, String modelo, int añoDeFabricacion, double kilometraje, String us){
        super(fabricante, modelo, añoDeFabricacion, kilometraje);
        this.uso = us;
    }

    public String getUso(){
        return this.uso;
    }

    @Override
    public String toString() {
        return "Motocicleta: " + modelo + " - Motocicleta: " + uso;
    }

}
