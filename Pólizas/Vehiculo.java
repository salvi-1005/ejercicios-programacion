public class Vehiculo {

    private String patente;
    private int añoFabricacion;
    private double montoCompra;

    public Vehiculo(String patente, int añoFabricacion, double montoCompra) {
        this.patente = patente;
        this.añoFabricacion = añoFabricacion;
        this.montoCompra = montoCompra;
    }

    public String getPatente() {
        return patente;
    }

    public int getAñoFabricacion() {
        return añoFabricacion;
    }

    public double getMontoCompra() {
        return montoCompra;
    }

    public void setPatente(String patente) {
        this.patente = patente;
    }

    public void setAñoFabricacion(int añoFabricacion) {
        this.añoFabricacion = añoFabricacion;
    }

    public void setMontoCompra(double montoCompra) {
        this.montoCompra = montoCompra;
    }

    public String toString() {
        return "- Patente: " + patente + 
               ", - Anio de Fabricacion: " + añoFabricacion + 
               ", - Monto de Compra: " + montoCompra;
    }
}
