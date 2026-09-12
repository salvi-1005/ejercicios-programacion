import java.time.LocalDate;

public class Donacion {

    private Donante donante;
    private LocalDate fecha;
    private double monto;
    private int id; //Se le asigna un ID luego de ser registrada en la organización, para evitar que se asignen IDs a donaciones que no han sido registradas.
    private Estado estado; //El estado de la donación, que puede ser "PENDIENTE", "RECHAZADA" o "COBRADA". Se asigna un estado inicial de "PENDIENTE" al momento de registrar la donación.

    public Donacion(Donante donante, LocalDate fecha, double monto){
        this.donante = donante;
        this.fecha = fecha;
        this.monto = monto;
        this.estado = Estado.PENDIENTE; //Se asigna un estado inicial de "PENDIENTE" al momento de registrar la donación.
        this.id = 0; //Se le asigna un ID luego de ser registrada en la organización, para evitar que se asignen IDs a donaciones que no han sido registradas.
    }

    public Donante getDonante() {
        return donante;
    }

    public LocalDate getFecha() {
        return fecha;
    }

    public double getMonto() {
        return monto;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Estado getEstado() {
        return estado;
    }

    public void setCobrada() {
        this.estado = Estado.COBRADA;
    }

    public void setRechazada() {
        this.estado = Estado.RECHAZADA;
    }

    public enum Estado {
        PENDIENTE, RECHAZADA, COBRADA
    }

    public String toString(){
        return "- Donante: " + donante.toString() + 
               " - fecha " + fecha +                                                
               " - Estado: " + estado + 
               " - Monto: " + monto;
    }
    
}
