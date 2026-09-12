import java.time.LocalDate;

public abstract class Poliza {

    protected Cliente cliente;
    protected double montoAsegurado;
    protected LocalDate fechaInicio;
    protected LocalDate fechaFin;

    public Poliza(Cliente cliente, double montoAsegurado, LocalDate fechaInicio, LocalDate fechaFin) {
        this.cliente = cliente;
        this.montoAsegurado = montoAsegurado;
        this.fechaInicio = fechaInicio;
        this.fechaFin = fechaFin;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public double getMontoAsegurado() {
        return montoAsegurado;
    }

    public LocalDate getFechaInicio() {
        return fechaInicio;
    }

    public LocalDate getFechaFin() {
        return fechaFin;
    }

    public void setMontoAsegurado(double montoAsegurado) {
        this.montoAsegurado = montoAsegurado;
    }

    public void setFechaInicio(LocalDate fechaInicio) {
        this.fechaInicio = fechaInicio;
    }

    public void setFechaFin(LocalDate fechaFin) {
        this.fechaFin = fechaFin;
    }

    public boolean estaVigente() {
        LocalDate hoy = LocalDate.now();
        return !hoy.isBefore(fechaInicio) && !hoy.isAfter(fechaFin);
    }

    public abstract double calcularCostoAnual();

    public String toString() {
        return "-- Poliza -- " +
               "- Cliente: " + cliente.getNombre() + " " + cliente.getApellido() + 
               ", - Edad: " + cliente.calcularEdad() + " anios" +
               ", - Monto Asegurado: " + montoAsegurado + 
               ", - Costo Anual: " + calcularCostoAnual() +
               ", - Fecha de vigencia Inicial: " + fechaInicio +
               ", - Fecha de vigencia Final: " + fechaFin + 
               ", - ¿Esta vigente?: " + (estaVigente() ? ", SI" : " - NO") +
               ", -- Vehiculo -- " + 
               (this instanceof Automotor ? ((Automotor) this).getVehiculo().toString() : "N/A");
    }
 
}
