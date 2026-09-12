import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class Vida extends Poliza {


    public Vida(Cliente cliente, double montoAsegurado, LocalDate fechaInicio, LocalDate fechaFin) {
        super(cliente, montoAsegurado, fechaInicio, fechaFin);
    }

    public double calcularCostoAnual() {
        if (ChronoUnit.YEARS.between(cliente.getFechaNacimiento(), fechaInicio) < 35){
            return montoAsegurado * 0.05; // 5% del monto para menores de 35 años
        } else {
            return montoAsegurado * 0.1; // 10% del monto para mayores de 35 años
        }
    }

}
