import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class Automotor extends Poliza {

    private Vehiculo vehiculo;

    public Automotor(Cliente cliente, double montoAsegurado, LocalDate fechaInicio, LocalDate fechaFin, Vehiculo vehiculo) {
        super(cliente, montoAsegurado, fechaInicio, fechaFin);
        this.vehiculo = vehiculo;
    }

    public Vehiculo getVehiculo() {
        return vehiculo;
    }

    public double calcularCostoAnual() {
        int antiguedad = LocalDate.now().getYear() - vehiculo.getAñoFabricacion();
        double valorBase = vehiculo.getMontoCompra();
        double descuento = antiguedad * 0.05 * valorBase; // 5% de descuento por año de antigüedad
        setMontoAsegurado(valorBase - descuento);
        if (ChronoUnit.YEARS.between(cliente.getFechaNacimiento(), fechaInicio) < 30)
            return montoAsegurado * 0.20;
        else
            return montoAsegurado * 0.10;
    }

       
        
    

}
