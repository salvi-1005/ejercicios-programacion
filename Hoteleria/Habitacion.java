public class Habitacion {

    private int numeroDeHabitacion;
    private Cliente cliente;

    public Habitacion(int numeroDeHabitacion) {
        this.numeroDeHabitacion = numeroDeHabitacion;
        this.cliente = null;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public int getNumeroDeHabitacion() {
        return numeroDeHabitacion;
    }

    
}
